
# 요구하는 범위 안에 정수를 입력받자.

while True :
    data = int(input('입력 : '))
    if data >= 1 and data <= 100 :
        break
    else :
        print('1~100사이의 값을 입력해주세요.')

i = 1; total = 0
while i <= data :
    total += i
    i += 1
print('1 ~ {}의 합계 : {}'.format(data ,total))