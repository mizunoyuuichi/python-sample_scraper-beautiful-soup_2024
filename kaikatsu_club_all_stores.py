import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1 ローカルファイルを指定

#list_url = "https://www.kaikatsu.jp/shop/result.html?"
#response = requests.get(list_url)
#soup = BeautifulSoup(response.content, 'html.parser')

soup = BeautifulSoup(open('快活CLUB店舗.html'), 'html.parser')

# 2 繰り返し表示に使われているタグを指定
articles = soup.find_all('article')

# 3 ループで配列に抽出
stores = []
for article in articles:
    title = article.find('h3')
    # ... find や find_all を重ねて 掘り出していく
    addres = article.find('ul').find('li').find_all('p')[1]
    # ...`{ key: value, ... }`で レコード扱いになるらしい
    stores.append({ "店舗名": '快活クラブ  ' + title.text, "住所": addres.text })

# 4 リストをCSVに書き出し
df = pd.DataFrame(stores)
csv_path = 'kaikatsu_club_all_stores.csv'
df.to_csv(csv_path, index=False, encoding='utf-8')
print(f"CSVファイルが作成されました：{csv_path}")
