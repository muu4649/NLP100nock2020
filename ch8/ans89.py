from tqdm import tqdm
import torch
from torch import optim
from torchtext import data
from transformers import BertForSequenceClassification


def eval_net(model, data_loader, device='cpu'):
    model.eval()
    ys = []
    ypreds = []
    
    for batch in test_iter:
        x, y = batch.TEXT, batch.LABEL
        with torch.no_grad():
            loss, logit = model(input_ids=x, labels=y)
            _, y_pred = torch.max(logit, 1)
        ys.append(y)
        ypreds.append(y_pred)
    ys = torch.cat(ys)
    ypreds = torch.cat(ypreds)
    print(f'test acc: {(ys == ypreds).sum().item() / len(ys)}')
    return


TEXT = data.Field(sequential=True, lower=True, batch_first=True)
LABELS = data.Field(sequential=False, batch_first=True, use_vocab=False)

train, test = data.TabularDataset.splits(
    path='./', train='trainel.tsv',
    test='testel.tsv', format='tsv',
    fields=[('TEXT', TEXT), ('LABEL', LABELS)])

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
train_iter, test_iter = data.Iterator.splits(
    (train, test), batch_sizes=(32, 32), device=device, repeat=False, sort=False)

TEXT.build_vocab(train, min_freq=2)
LABELS.build_vocab(train)

model = BertForSequenceClassification.from_pretrained('bert-base-japanese-whole-word-masking', num_labels=2)
model = model.to(device)

optimizer = optim.SGD(model.parameters(), lr=0.01)



for name, param in model.named_parameters():
    param.requires_grad = True
"""
# Bert encoderの最終レイヤのrequires_gradをTrueで更新
for name, param in model.bert.encoder.layer[-1].named_parameters():
    param.requires_grad = True

# 最後のclassificationレイヤのrequires_gradをTrueで更新
for name, param in model.classifier.named_parameters():
    param.requires_grad = True
"""



for epoch in tqdm(range(10)):
    losses = []
    model.train()
    for batch in train_iter:
        x, y = batch.TEXT, batch.LABEL
        loss, logit = model(input_ids=x, labels=y)
        model.zero_grad()
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        _, y_pred_train = torch.max(logit, 1)
    eval_net(model, test_iter, device)
