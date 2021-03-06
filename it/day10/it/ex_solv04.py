'''
1~1000까지의 합을 구하시오.
단 3의 배수는 제외하고 3의 배수이면서 5의 배수는
제외하지 않는 조건으로 구하시오
'''

sum = 0
for i in range(1 , 1000) :
    if i % 3 == 0 :
        if i % 5 == 0 :
            sum += i
    else :
        sum += i
print("결과 :",sum)

'''선생님 풀이'''

total = 0
for i in range(1,1001) :
    if i % 3 == 0 and i % 5 == 0 :
        total += i
    elif i % 3 != 0 :
        total += i
print("합계 : {}".format(total))


