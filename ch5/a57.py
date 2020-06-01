#52で学習したロジスティック回帰モデルの中で，重みの高い特徴量トップ10と，重みの低い特徴量トップ10を確認せよ．

import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


#X_train = pd.read_table('train.feature.txt', header=None)
#y_train = pd.read_table('train2.txt', header=None)[1]
clf = joblib.load('model.joblib')
vocabulary_ = joblib.load('vocabulary_.joblib')
coefs = clf.coef_
for c in coefs:
    d = dict(zip(vocabulary_, c))
    d_top = sorted(d.items(), key=lambda x: abs(x[1]), reverse=True)[:10]
    print(d_top)
    d_bottom = sorted(d.items(), key=lambda x: abs(x[1]), reverse=False)[:10]
    print(d_bottom)
