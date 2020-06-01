#動詞の原形をすべて抽出せよ
from a30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for morpheme in morphemes:
        if morpheme["pos"] == "動詞":
            result.append(morpheme["base"])

print(result[:10])
