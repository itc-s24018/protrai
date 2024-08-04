# s24018
# 沖縄県の推計人口のページより基礎情報をスクレイピングするPythonコード
import requests
from bs4 import BeautifulSoup as bs

uri = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
html = requests.get(uri)

html.encoding = "Shift_JIS"

soup = bs(html.text, 'html.parser')
baseElement = soup.find('table', class_='table1 font2 gyo5')

population = [
  "",
  "",
  "",
  ""
]

for i, element in enumerate(baseElement.find_all("td", align="right")):
  population[i] = element.text

print("沖縄県の推計人口")
print(f"総人口: {population[0]}")
print(f"男: {population[1]}")
print(f"女: {population[2]}")
