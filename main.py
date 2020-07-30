# pip install requests
# pip install beautifulsoup4
# beautifulsoupのバージョンは４ということ。python3では4以下を使うことができない

import requests  # http通信を行うもの
from bs4 import BeautifulSoup  #習得したWEBページの情報を整形し、狙った情報を抽出

# 1:HTTP通信の確認 
url1 = 'https://www.google.co.jp/'
res1 = requests.get(url1)
print(res1)
print(res1.text)



# 2:HTTPにリクエストして、検索をかける
url2 = 'https://www.google.co.jp/search'
p = {'q':'cat'}
res2 = requests.get(url2, params=p) #キーワード引数paramsに付与したいパラメータを辞書オブジェクトで指定できる 
print(res2.url)
print(res2.text)

# 3:beautifulsoupを使ってみる(これより以下のコードは直下のコードを基盤としている)
url1 = 'https://www.google.co.jp/'
res1 = requests.get(url1)
html_text = res1.text
soup = BeautifulSoup(html_text)  # BeautifulSoupオブジェクト

# ________タイトル取得________
# print(soup.prettify())  #HTMLを1行1タグに整形されたUnicode文字列(prettify()メソッドの仕事)
print(soup.title)  #出力：<title>Google</title>
print(soup.title.name)  #出力：title
print(soup.title.string)  #出力；Google

# ________aタグ全取得_________
print(soup.find_all('a'))

# _______aタグかつclass="gb1"の要素全取得______
print(soup.find_all('a', class_="gb1"))

# ______辞書オブジェクトで要素の属性をしてすることもできる______
print(soup.find_all('a', attrs={'class':'gb4'}))  #1つしか出来ない。辞書オブジェクトに複数入れることは出来るが、結果出力は最後に指定されたものである。{'class':'gb4','class':'gb1'} -> class:gb1 の結果

# _____CSSセレクタによる要素取得_____
print(soup.select('.gb4'))
