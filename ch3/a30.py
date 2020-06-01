#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
def get_neko_morphemes():
    morphemes_list = []
    with open("neko.txt.mecab") as f:
        morphemes = []
        for i, line in enumerate(f):
            split_line = line.rstrip("\r\n").split("\t")
            if len(split_line) == 1:
                if len(morphemes) != 0:
                    morphemes_list.append(morphemes)
                    morphemes = []
                continue
            morpheme_map = split_line[1].split(",")
            morpheme = {
                "surface": split_line[0],
                "base": morpheme_map[6],
                "pos": morpheme_map[0],
                "pos1": morpheme_map[1],
            }
            morphemes.append(morpheme)
        else:
            if len(morphemes) != 0:
                morphemes_list.append(morphemes)

    return morphemes_list


if __name__ == "__main__":
    from pprint import pprint
    result = get_neko_morphemes()
    pprint(result[:10])
