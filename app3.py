import requests
from bs4 import BeautifulSoup
import urllib.request

# 데이터 = requests.get('https://www.google.com/finance/quote/005930:KRX?hl=ko')
# soup = BeautifulSoup(데이터.content, 'html.parser')
# print(soup.find_all('div', class_='kf1m0')[0].text.replace('₩',''))


데이터 = requests.get('https://finance.naver.com/item/sise.naver?code=005930')
soup = BeautifulSoup(데이터.content, 'html.parser')
print(soup.find_all('strong', id='_nowVal')[0].text)
print(soup.find_all('span', id = '_quant')[0].text)

print(soup.select('.f_down em')[0].text)

이미지 = soup.select('#img_chart_area')[0]
print(이미지['src'])
urllib.request.urlretrieve('https://ssl.pstatic.net/imgfinance/chart/item/area/day/005930.png?sidcode=1729069377049', '차트.jpg')
