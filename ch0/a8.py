#引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ

def alarm(x,y,z):
    a = str(x)+'時の'+y+'は'+str(z)
    return a
x=12
y='気温'
z=22.4

print(alarm(x,y,z))
