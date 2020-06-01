#2つの名詞が「の」で連結されている名詞句を抽出せよ．
from a30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for i in range(1,len(morphemes)-1):
        if morphemes[i]["base"] == "の":
            continue
        before=morphemes[i-1]
        after=morphemes[i+1]
        if before["pos"] == "名詞":
            if after["pos"] == "名詞":
                result.append(before["surface"] + "の" + after["surface"])
print(result[:10])
