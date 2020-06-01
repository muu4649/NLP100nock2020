#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import pandas as pd

df = pd.read_json('jawiki-country.json.gz', lines=True)
ukText = df.query('title=="イギリス"')['text'].values[0]
ukTextList = ukText.split('\n')
ans = list(filter(lambda x: 'Category:' in x, ukTextList))
ans = [a.replace('[[Category:', '').replace('|*', '').replace(']]', '') for a in ans]
print(ans)
