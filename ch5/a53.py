import pandas as pd
from sklearn.linear_model import LogisticRegression


X_train = pd.read_table('train.feature.txt', header=None)
y_train = pd.read_table('train2.txt', header=None)[1]

clf = LogisticRegression(penalty='l2', solver='sag', random_state=0)
clf.fit(X_train, y_train)
y_train = clf.predict(X_train)

print(y_train)
