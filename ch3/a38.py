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
plt.hist(word_count, bins=50, range=(1, 50))
plt.savefig("fig38.png")
