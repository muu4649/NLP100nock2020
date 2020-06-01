#40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．


class Morph:
    def __init__(self, dc):
        self.surface = dc['surface']
        self.base = dc['base']
        self.pos = dc['pos']
        self.pos1 = dc['pos1']


class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs    # 形態素（Morphオブジェクト）のリスト
        self.dst = dst          # 係り先文節インデックス番号
        self.srcs = []          # 係り元文節インデックス番号のリスト


def parseCabocha(block):
    def checkCreateChunk(tmp):
        if len(tmp) > 0:
            c = Chunk(tmp, dst)
            res.append(c)
            tmp = []
        return tmp

    res = []
    tmp = []
    dst = None
    for line in block.split('\n'):
        if line == '':
            tmp = checkCreateChunk(tmp)
        elif line[0] == '*':
            dst = line.split(' ')[2].rstrip('D')
            tmp = checkCreateChunk(tmp)
        else:
            (surface, attr) = line.split('\t')
            attr = attr.split(',')
            lineDict = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1]
            }
            tmp.append(Morph(lineDict))

    for i, r in enumerate(res):
        res[int(r.dst)].srcs.append(i)
    return res


filename = './neko.txt.cabocha'
with open(filename, mode='rt', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = list(filter(lambda x: x != '', blockList))
blockList = [parseCabocha(block) for block in blockList]
for m in blockList[7]:
    print([mo.surface for mo in m.morphs], m.dst, m.srcs)
