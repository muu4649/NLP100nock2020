#“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ

def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]
n=2
text1='paraparaparadise'
text2='paragraph'

X=set(n_gram(text1,n))
Y=set(n_gram(text2,n))
dif=X.difference(Y)
uni=X.union(Y)
seki=X.intersection(Y)

print(dif,uni,seki)
print('se' in uni)

