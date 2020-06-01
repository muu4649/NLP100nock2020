#記事中でカテゴリ名を宣言している行を抽出せよ
#https://it-engineer-lab.com/archives/124
import pandas as pd


df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
ukTextList = ukText.split('\n')
ans = list(filter(lambda x: 'Category:' in x, ukTextList))
print(ans)
