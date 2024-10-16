# 파일 = open('a.txt', 'w')
# 파일.write('hello')
# 파일.close()

# 파일 = open('a.txt', 'a')
# 파일.write('반가워')
# 파일.close()

# 파일 = open('a.txt', 'r')
# print(파일.read())
# 파일.close()


f = open('data.csv', 'w')
f.write('김, 이, 박')
f.write('\n김, 이, 박')
f.close()

f = open('data.csv', 'r')
print(f.read())
f.close()

리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']
company = open('company.txt', 'w')
for i in 리스트:
    company.write(f'{i}\n')
company.close()

company = open('company.txt', 'r')
print(company.read())
company.close()

# 구구단
for i in range(1,10):
    for j in range(2,10):
        print(f'{j}*{i}={j*i:3d}', end= '  ')
        if j==9:
            print('\n')
