#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．．
from a30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for i in range(1,len(morphemes)-1):
        after=morphemes[i+1]
        if morphemes[i]["pos"] == "名詞":
            if after["pos"] == "名詞":
                result.append(morphemes[i]["surface"] + after["surface"])
                print(result)
print(sorted(result, reverse=True, key=len))
