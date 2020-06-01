#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
import numpy as np

def word_gram(text,n):
    gram = np.zeros(0)
    for i, w in enumerate(text):
        gram = np.append(gram,text[i:i+n])
        
    return gram

def moji_gram(text,n):
     
    gram = np.zeros(0)
    a=text.split(' ')

    for i, w in enumerate(text.split(' ')):
        gram = np.append(gram,a[i:i+n])
        
    return gram
def n_gram(target, n):
    target=target.split(' ')
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]



text = 'I am an NLPer'
n=2
print(word_gram(text,2))

print(moji_gram(text,2))


print(n_gram(text,2))
