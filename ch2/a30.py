#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

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

import urllib.request
# dct_country は Q20 にて取得済みとする
match = re.findall('^\{\{基礎情報(.*?)\}\}$',dct_country.get('text'),re.MULTILINE+re.DOTALL)
match2 = re.findall('\|(.*?) = (.*?)\n',match[0])
match_dct = dict(match2)

image_name = re.sub('\[\[ファイル:(.*?)\|.*\]\]','\\1',match_dct['国章画像']) # ファイル名を抽出
param = {
    'format': 'json',
    'action': 'query',
    'titles': 'File:Royal%20Coat%20of%20Arms%20of%20the%20United%20Kingdom.svg',
    'prop': 'imageinfo',
    'iiprop': 'url'
}
query = '&'.join("%s=%s" % (k, v) for k, v in param.items())
url = 'http://en.wikipedia.org/w/api.php?%s'  % (query)
request = urllib.request.urlopen(url)
jsonData = request.read().decode('utf-8')
data = json.loads(jsonData)
print(data.get('query').get('pages').get('-1').get('imageinfo')[0].get('url'))
