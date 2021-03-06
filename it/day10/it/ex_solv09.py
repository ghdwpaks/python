'''
첫날에 1원을 예금하고, 다음날에는 전날의 2배씩 증가하는 방식이다.
30일째 되는 날 예금해야 하는 금액을 구하시오
'''
s = 0
for i in range(1 , 31) :
    s += i
    s *= 2
print("30일째 되는 날 예금해야 하는 금액 :",s)


'''선생님 답안'''
total = 0; seed = 1
for i in range(1,31) :
    total += seed
    seed *= 2
print("저축 금액 :{:,}원".format(total))

