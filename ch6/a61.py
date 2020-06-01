#“United States”と”U.S.”のコサイン類似度を計算せよ．

import numpy as np
from gensim.models import KeyedVectors

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
us = model['United_States']
us1 = model['U.S.']

print(cos_sim(us,us1))
