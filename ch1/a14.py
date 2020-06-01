#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
import pandas as pd
import sys


df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
num = int(sys.argv[1])
print(df.head(num))

