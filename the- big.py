import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1 ローカルファイルを指定

list_url_1 = "https://www.mapion.co.jp/phonebook/M02002CL32/"
list_url_2 = "https://www.mapion.co.jp/phonebook/M02002CL32/2.html"
list_url_3 = "https://www.mapion.co.jp/phonebook/M02002CL32/3.html"
list_url_4 = "https://www.mapion.co.jp/phonebook/M02002CL32/4.html"
list_url_5 = "https://www.mapion.co.jp/phonebook/M02002CL32/5.html"
list_url_6 = "https://www.mapion.co.jp/phonebook/M02002CL32/6.html"
list_url_7 = "https://www.mapion.co.jp/phonebook/M02002CL32/7.html"
list_url_8 = "https://www.mapion.co.jp/phonebook/M02002CL32/8.html"

response = requests.get(list_url_8)
soup = BeautifulSoup(response.content, 'html.parser')

# 2 繰り返し表示に使われているタグを指定
articles = soup.find_all('tr')

# 3 ループで配列に抽出
stores = []
for article in articles:
	title = article.find('th').find('a')
	# find や find_all を重ねて 掘り出していく
	addres = article.find('td')

	if title is None or addres is None:
		# タイトルまたは住所がない場合はスキップ
		continue

	#`{ key: value, ... }`で レコード扱いになるらしい
	stores.append({ "店舗名": title.text, "住所": addres.text })

# 4 リストをCSVに書き出し
df = pd.DataFrame(stores)
csv_path = 'max_value_8.csv'
df.to_csv(csv_path, index=False, encoding='utf-8')
print(f"CSVファイルが作成されました：{csv_path}")

