import json
import requests

# JSON 데이터가 있는 URL
url = 'https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR&lgl_rcode=04290127&fgn_region=&fgn_city=&lgl_lat=35.824&lgl_long=128.7556&enlu_query=IggCAASCULgQAAAA%2FN0XP6rsZ5VdHM76o2fHow%2B%2B5e57TSpq7rS9AT9aainDISv4TSRj2IQuAugtb5oP&enqx_theme=IggCAGSCULjGAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn72sYuS%2Bm6ucJK%2FQ6Nr3ChAnuxhwUE%2FPNELIrhFnaDTJhWSDv7n%2Ff7J98yUxvJxPwY%3D&abt=&retry_count=0'

# URL에서 JSON 데이터 가져오기
response = requests.get(url)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    response.encoding = 'utf-8'  # 응답 인코딩 설정
    data = response.text

    # JSON 파싱
    parsed_data = json.loads(data)

    # HTML 추출 및 디코딩
    html_content = parsed_data["contents"].encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')


    # HTML 파일로 저장
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("HTML 파일로 저장되었습니다. 'output.html'을 열어보세요.")
else:
    print(f"데이터를 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
