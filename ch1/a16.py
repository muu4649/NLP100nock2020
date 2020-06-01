#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ

import sys
import pandas as pd


if len(sys.argv) == 1:
    print('Set arg n, like "python ans15.py 5"')
else:
    df = pd.read_csv('./popular-names.txt', sep='\t', header=None)
    n = int(sys.argv[1])
    nrow = -(-len(df) // n #//は切り捨て)
    for i in range(n):
        df.loc[nrow * i:nrow * (i + 1)].to_csv(f'ans16_{i}', sep='\t', index=iFalse, header=None)
