import requests
from bs4 import BeautifulSoup
for num in range(4):
    n = num*3 + 1
    prank = n+30
    data = requests.get(f'https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start={n}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR&lgl_rcode=04290127&fgn_region=&fgn_city=&lgl_lat=35.824&lgl_long=128.7556&enlu_query=IggCAASCULgQAAAA%2FN0XP6rsZ5VdHM76o2fHow%2B%2B5e57TSpq7rS9AT9aainDISv4TSRj2IQuAugtb5oP&enqx_theme=IggCAGSCULjGAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn72sYuS%2Bm6ucJK%2FQ6Nr3ChAnuxhwUE%2FPNELIrhFnaDTJhWSDv7n%2Ff7J98yUxvJxPwY%3D&abt=&retry_count=0')

    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')
    글리스트 = soup.select('a.title_link')
    for i in range(30):
        print(i)
        print(글리스트[i].text)

data = requests.get('https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR&lgl_rcode=04290127&fgn_region=&fgn_city=&lgl_lat=35.824&lgl_long=128.7556&enlu_query=IggCAASCULgQAAAA%2FN0XP6rsZ5VdHM76o2fHow%2B%2B5e57TSpq7rS9AT9aainDISv4TSRj2IQuAugtb5oP&enqx_theme=IggCAGSCULjGAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn72sYuS%2Bm6ucJK%2FQ6Nr3ChAnuxhwUE%2FPNELIrhFnaDTJhWSDv7n%2Ff7J98yUxvJxPwY%3D&abt=&retry_count=0')
