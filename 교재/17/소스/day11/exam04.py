

while True :
    data = int(input('입력 : '))
    if data >= 1 and data <= 100 :
        break
    else :
        print('1~100사이의 값을 입력해주세요.')

i = 0; total = 0
while i < data :
    i += 1
    if i % 2 == 0 :
        continue
    total += i
   
    
print('1 ~ {}의 홀수 합계 : {}'.format(data ,total))

i = 1; total = 0
while i <= 10 :
    total += i
    i += 2
print('1 ~ 10 범위의 홀수 합계 : {}'.format(total))