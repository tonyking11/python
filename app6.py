import time


시간 = time.time()
시간 = time.ctime(시간)

시간 = time.localtime()
a = time.strftime('%Y년 %m월', 시간)
print(a)

name = 'Kim'
print(f'안녕하세요{name}')


import datetime
a = datetime.datetime(2022, 10, 1)
print(datetime.datetime.now())
