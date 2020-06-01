#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
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
        #print(dct_country.get('text'))
        break

    # dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
match_dct2 = {}
for key,value in match_dct.items():
     match_dct2[key] = re.sub('\'\'+','',value)

print (match_dct2)
