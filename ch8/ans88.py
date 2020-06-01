#define by runについて https://qiita.com/GushiSnow/items/aa660c7228b7024076a8
import torch
from torch import nn, optim
from torchtext import data
from catalyst.dl import SupervisedRunner
from catalyst.dl.callbacks import AccuracyCallback
from torch.utils.data import DataLoader
from torchtext.data import Iterator
from gensim.models import KeyedVectors
from torchsummary import summary

class BucketIteratorWrapper(DataLoader):
    __initialized__ = False

    def __init__(self, iterator: Iterator):
        self.batch_size = iterator.batch_size
        self.num_workers = 1
        self.collate_fn = None
        self.pin_memory = False
        self.drop_last = False
        self.timeout = 0
        self.worker_init_fn = None
        self.sampler = iterator
        self.batch_sampler = iterator
        self.__initialized__ = True

    def __iter__(self):
        return map(lambda batch: {
            'features': batch.TEXT,
            'targets': batch.LABEL,
        }, self.batch_sampler.__iter__())

    def __len__(self):
        return len(self.batch_sampler)


class RNN(nn.Module):
    def __init__(self, num_embeddings,
                 embedding_dim=300,
                 hidden_size=100,
                 output_size=1,
                 num_layers=1,
                 dropout=0.2):
        super().__init__()
        model = KeyedVectors.load_word2vec_format('../ch6/GoogleNews-vectors-negative300.bin', binary=True)
        weights = torch.FloatTensor(model.vectors)
        self.emb = nn.Embedding.from_pretrained(weights)
        #https://www.it-swarm.dev/ja/python/pytorch-gensim事前学習済みのword埋め込みを読み込む方法/836977893/
        self.lstm = nn.LSTM(embedding_dim,
                            hidden_size, num_layers,
                            batch_first=True, dropout=dropout, bidirectional=True)
        self.linear = nn.Sequential(
            nn.Linear(hidden_size * 2, 50),
            nn.PReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, output_size)
        )

    def forward(self, x, h0=None):
        x = self.emb(x)
        x, h = self.lstm(x, h0)
        x = x[:, -1, :]
        x = self.linear(x)
        return x


#####前処理######
TEXT = data.Field(sequential=True, lower=True, batch_first=True)
LABELS = data.Field(sequential=False, batch_first=True, use_vocab=False)

train, val, test = data.TabularDataset.splits(
    path='../ch5', train='train2.txt',
    validation='valid2.txt', test='test2.txt', format='tsv',
    fields=[('TEXT', TEXT), ('LABEL', LABELS)])

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
train_iter, val_iter, test_iter = data.BucketIterator.splits(
    (train, val, test), batch_sizes=(64, 64, 64), device=device, repeat=False, sort=False)

train_loader = BucketIteratorWrapper(train_iter)
valid_loader = BucketIteratorWrapper(val_iter)
loaders = {"train": train_loader, "valid": valid_loader}

TEXT.build_vocab(train, min_freq=2)#辞書作成
LABELS.build_vocab(train)#ラベル側にも

###モデル定義
model = RNN(len(TEXT.vocab.stoi) + 1, num_layers=1, output_size=4)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
#summary(model, (3, 224, 224))
#quit()
runner = SupervisedRunner()

runner.train(
    model=model,
    criterion=criterion,
    optimizer=optimizer,
    loaders=loaders,
    logdir="./logdir",
    callbacks=[AccuracyCallback(num_classes=4, accuracy_args=[1])],
    num_epochs=5,
    verbose=True,
)
