#52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ．カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能をマイクロ平均（micro-average）とマクロ平均（macro-average）で統合せよ．

import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


#X_train = pd.read_table('train.feature.txt', header=None)
#y_train = pd.read_table('train2.txt', header=None)[1]

X_test = pd.read_table('test.feature.txt', header=None)
y_test = pd.read_table('test2.txt', header=None)[1]
clf = joblib.load('model.joblib')

y_pred=clf.predict(X_test)
print("マクロ平均適合率",precision_score(y_pred,y_test,average='macro'),"マイクロ平均適合率",precision_score(y_pred,y_test,average='micro'))
print("マクロ平均再現率",recall_score(y_pred,y_test,average='macro'),"マイクロ平均再現率",recall_score(y_pred,y_test,average='micro'))
print("マクロf1",f1_score(y_pred,y_test,average='macro'),"マイクロf1",f1_score(y_pred,y_test,average='micro'))


