#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考:
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

match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)
match_tmp = ''
match_tmp2 = ''
match_dct2 = {}
for key,value in match_dct.items():
    match_tmp = re.sub('\'\'+','',value) # 強調を除去
    match_tmp = re.sub('\[\[(.*?)([|\|].*)?\]\]','\\1',match_tmp) # リンクを除去
    match_dct2[key] = match_tmp

print (match_dct2)
