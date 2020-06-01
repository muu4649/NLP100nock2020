"""
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを
"""



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


filename = 'neko.txt.cabocha'
with open(filename, mode='rt', encoding='utf-8') as f:
    blockList = f.read().split('EOS\n')
blockList = list(filter(lambda x: x != '', blockList))
blockList = [parseCabocha(block) for block in blockList]

for b in blockList:
    for m in b:
        if len(m.srcs) > 0:
            preMorphs = [b[int(s)].morphs for s in m.srcs]
            preMorphsFiltered = [list(filter(lambda x: '助詞' in x.pos, pm)) for pm in preMorphs]
            preSurface = [[p.surface for p in pm] for pm in preMorphsFiltered]
            preSurface = list(filter(lambda x: x != [], preSurface))
            preSurface = [p[0] for p in preSurface]
            postBase = [mo.base for mo in m.morphs]
            postPos = [mo.pos for mo in m.morphs]
            if len(preSurface) > 0 and '動詞' in postPos:
                preText = list(filter(lambda x: '助詞' in [p.pos for p in x], preMorphs))
                preText = [''.join([p.surface for p in pt]) for pt in preText]
                print(postBase[0], ' '.join(preSurface), ' '.join(preText), sep='\t')
