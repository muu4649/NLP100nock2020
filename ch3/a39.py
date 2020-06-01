#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

from a30 import get_neko_morphemes
from collections import Counter
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


morphemes_list = get_neko_morphemes()

result = []
words = Counter([morpheme["base"] for morphemes in morphemes_list for morpheme in morphemes]).most_common()
_, word_count = list(zip(*words))

plt.rcParams["font.family"] = "IPAexGothic"
plt.plot(list(range(1, len(word_count) + 1)), word_count)
plt.xscale("log")
plt.yscale("log")
plt.savefig("fig39.png")
