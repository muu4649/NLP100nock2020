#記事から参照されているメディアファイルをすべて抜き出せ
import re
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
for file in re.findall(r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]', ukText):
    print(file[1])
