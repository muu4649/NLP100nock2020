#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
import gzip,json
import re
with gzip.open('./jawiki-country.json.gz',mode='rt',encoding='utf=8') as gz_temp:
     jsonlines = gz_temp.read()

lst_country = []
for line in jsonlines.split('\n'):
    if len(line) > 1: # 空行がエラーになるため
      lst_country.append(json.loads(line))

for dct_country in lst_country:
    if dct_country.get('title') == 'イギリス':
        print(dct_country.get('text'))
        break

    # dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
print (match_dct)
# {'略名': 'イギリス', '日本語国名': 'グレートブリテン及び北アイルランド連合王国', '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>', '国旗画像': 'Flag of the United Kingdom.svg', '国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]', '国章リンク': '（
# (以下略)
