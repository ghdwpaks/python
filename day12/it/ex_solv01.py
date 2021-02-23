'''
1X2 - 2X3 + 3X4 - 4X5 + 5x6 와 같은 규칙으로
합계를 구할 때 합이 100이 넘는 마지막 수 2 개를 구하는 프로그램을 작성화여라
'''
i = 1
ic = 1#+ 또는 - 판별용 변수, 홀수이면 + 짝수이면 - 이다
t = 0 #total, 전체 계산 합계
r = 0 #1회전용 계산 합계
while True:
    
    r = i * (i+1)
    if ic % 2 == 0 :
        t -= r
    else :
        t += r
    if t > 100 :
        break
    i += 1
    ic += 1
print("100이 넘는 마지막 수 2개 = {} , {}".format(i,i+1))


'''선생님 답안'''
data = 1
total = 0
while True :
    if data  % 2 == 1 :
        total += data *(data +1 )
    else :
        total -= data * (data +1)
    print("{} x {} = {}".format(data,data+1,total))
    if total >= 100 :
        break
    data += 1
print("마지막 두 수는 {}와 {}이며, 합계는 {}입니다.".format(data ,data +1,total))
