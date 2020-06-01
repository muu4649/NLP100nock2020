#64の実行結果を用い，意味的アナロジー（semantic analogy）と文法的アナロジー（syntactic analogy）の正解率を測定せよ．

import pandas as pd


df = pd.read_csv('./ans64.txt', sep=' ', header=None)
print((df[3] == df[4]).sum() / len(df))
