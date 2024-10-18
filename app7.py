import requests
import json
import time
from multiprocessing.dummy import Pool as ThreadPool


url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def 함수(구멍):
    data = requests.get(구멍)
    딕셔너리 = json.loads(data.content)
    return 딕셔너리['data'][0]['Close']

for i in range(11):                                 # 리스트 내의 모든 자료에
    함수(url[0])                                    # 똑같은 작업을 시켜주고 싶을 때
                                                    # map() 쓰면 편할 수도
리스트 = [1,2,3,4,5,6]                              # map(리스트에 적용할 함수, 리스트))
def 더하기(x):
    return x+3

result = map(더하기, 리스트)
print(list(result))

pool = ThreadPool(4)
result = pool.map(함수, url) # 멀티쓰레딩을 쉽게 가능
pool.close()
pool.join()

print(result)
