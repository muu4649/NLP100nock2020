#“United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
import numpy as np
from gensim.models import KeyedVectors
model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
result = model.most_similar(positive=['United_States'])

for i in range(10):
    print("{}: {:.4f}".format(*result[i]))
