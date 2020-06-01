#国名に関する単語ベクトルを抽出し，k-meansクラスタリングをクラスタ数k=5として実行せよ
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


# http://www.fao.org/countryprofiles/iso3list/en/
country = pd.read_table('./countries.tcv')
country = country['Short name'].values

model = KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)

countryVec = []
countryName = []
for c in country:
    if c in model.vocab:
        countryVec.append(model[c])
        countryName.append(c)

X = np.array(countryVec)
km = KMeans(n_clusters=5, random_state=0)
y_km = km.fit_predict(X)
print(y_km)
