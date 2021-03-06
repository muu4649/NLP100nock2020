#「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
from a30 import get_neko_morphemes
from collections import Counter
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


morphemes_list = get_neko_morphemes()

result = []

for morphemes in morphemes_list:
    for i in range(1,len(morphemes)-1):
        after=morphemes[i+1]
        before=morphemes[i-1]
        if morphemes[i]["base"] == "猫":
            result.append(before["base"])
            result.append(after["base"])

words = Counter(result).most_common()
word_name, word_count = list(zip(*words[:10]))
print(word_name[:10])
plt.rcParams["font.family"] = "IPAexGothic"
plt.bar(range(10), word_count, tick_label=word_name)
plt.savefig("fig37.png")
