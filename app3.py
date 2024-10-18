import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import unicodedata #한글이랑 영어 
import csv

# 데이터 = requests.get('https://www.google.com/finance/quote/005930:KRX?hl=ko')
# soup = BeautifulSoup(데이터.content, 'html.parser')
# print(soup.find_all('div', class_='kf1m0')[0].text.replace('₩',''))

companylist = ['005930', '066575', '005380', '034220', '003490']
# for company in companylist:
def companydef(companynum):
    데이터 = requests.get(f'https://finance.naver.com/item/sise.naver?code={companynum}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    company_name = soup.select('div.wrap_company > h2 > a')[0].text
    company_price = soup.find_all('strong', id='_nowVal')[0].text
    company_dealmount = soup.find_all('span', id = '_quant')[0].text
    company_updownrate = re.sub(r'[\n\t]', '', soup.select('#tab_con1 div.gray td > em')[-1].text)
    return [company_name, company_price, company_dealmount, company_updownrate]

all_company_data = []
제목 = ['회사명', '현재가', '거래량', '등락률']
all_company_data.append(제목)

for company in companylist:
    company_data = companydef(company)
    all_company_data.append(company_data)


# 데이터 가로 정렬 방식으로 출력 및 파일 쓰기
with open('company.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 각 카테고리 별로 데이터를 가로로 나열
    for i in range(4):  # 총 4개의 항목 (회사명, 현재가, 거래량, 등락률)
        row = [company_data[i] for company_data in all_company_data]  # 모든 회사의 i번째 항목을 가져옴
        print(row)
        writer.writerow(row)
    


# 이미지 = soup.select('#img_chart_area')[0]
# print(이미지['src'])
# urllib.request.urlretrieve('https://ssl.pstatic.net/imgfinance/chart/item/area/day/005930.png?sidcode=1729069377049', '차트.jpg')
