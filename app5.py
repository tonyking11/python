import requests
import json
import time
num = 0
for epoch in range(11): 
    changingtime = 1728680400000 - 180000000*epoch
    data = requests.get(f'https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt={changingtime}&interval=15m&1729219775909')


    딕셔너리 =  json.loads(data.content)
    for i in range(len(딕셔너리['body']['candles'])):
        시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['body']['candles'][i]['dt']/1000))
        print(시간)
        가격 = f"{int(float(딕셔너리['body']['candles'][i]['close'])*10000)/10000:.4f}"
        print(가격)
    num = num+len(딕셔너리['body']['candles'])
print(f'자료갯수: {num}')
