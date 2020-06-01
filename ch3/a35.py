#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．．
from a30 import get_neko_morphemes
import numpy as np
from collections import Counter
morphemes_list = get_neko_morphemes()

words = Counter([morpheme["base"] for morphemes in morphemes_list for morpheme in morphemes]).most_common()
print(words[:10])
