#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
from collections import Counter
import matplotlib.pyplot as plt
from a30 import get_neko_morphemes

morphemes_list = get_neko_morphemes()

words = Counter([morpheme["base"] for morphemes in morphemes_list for morpheme in morphemes]).most_common()
word_name, word_count = list(zip(*words[:10]))

plt.rcParams["font.family"] = "IPAexGothic"
plt.bar(range(10), word_count, tick_label=word_name)
plt.show()
