# 1~1000까지의 합을 구하시오. 
# 단 3의 배수는 제외하고 3의 배수이면서 5의 배수는 
# 제외하지 않는 조건으로 구하시오
# 합계 : 366832

total = 0
for i in range(1, 1001) :
    if i % 3 == 0 and i % 5 == 0:
        total += i
    elif i % 3 != 0 :
        total += i

print('합계 : {}'.format(total))

# 두 수를 입력 받아 작은 수 ~ 큰 수의 합계를 출력하세요.
# 1 10
# 10 1
data1, data2 = input('두 수 입력 : ').split()
data1 = int(data1)
data2 = int(data2)

if data1 > data2 :
    tmp = data1
    data1 = data2
    data2 = tmp

total = 0
for i in range(data1, data2+1) :
    total += i
print('{} ~ {}의 합계 : {}'.format(data1, data2, total))
