

# 1. 입력된 수의 각 자리수의 합을 구하는 프로그램을 작성하라.
#  ex) 입력 : 12345
#      출력 : 15

data = int(input('입력 : '))
total = 0
while True :
    total = total + data % 10
    data = data // 10
    if data == 0 :
        break
print('합계 : {}'.format(total))

# 2. 입력된 수를 거꾸로 정수형 변수에 담아 출력하시오.(예 123 -> 321)
data = int(input('입력 : '))
total = 0
while True :
    total = total + data % 10 # 320
    data = data // 10
    if data == 0 :
        break
    total *= 10 # total = total * 10
print('입력 데이터 거꾸로 : {}'.format(total))

