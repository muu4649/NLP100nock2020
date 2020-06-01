#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
import random
import numpy as np
def randomize(text,n1,n2):
    a=text[n1]
    b=text[n2]
    
    c=text[n1+1:n2]
    random.shuffle(c)
    a=np.append(a,c)
    a=np.append(a,b)
    return a

text='I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
a=text.split(' ')
n1=0
n2=-1

print(randomize(a,n1,n2))

