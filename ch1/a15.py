#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
# coding:utf-8
import sys
import pandas as pd


if len(sys.argv) == 1:
    print('Set arg n, like "python ans15.py 5"')
else:
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    n = int(sys.argv[1])
    print(df.tail(n))

