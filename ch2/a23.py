#記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ
#https://murashun.jp/blog/20190215-01.html．
import pandas as pd
import re
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
for section in re.findall(r'(=+)([^=]+)\1\n', ukText):
    print(f'{section[1].strip()}\t{len(section[0]) - 1}')
