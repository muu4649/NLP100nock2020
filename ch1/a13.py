#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
import pandas as pd


df1 = pd.read_csv('./col1.txt', sep='\t', header=None)
df2 = pd.read_csv('./col2.txt', sep='\t', header=None)
print(df1)
df3 = pd.concat([df1, df2],axis=1)

df3.to_csv('ans13.txt', sep=' ', index=False, header=None)
