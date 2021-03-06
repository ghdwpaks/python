'''
1 ~ 10 까지의 합계를 구해주세요.
'''
sum = 0 
for i in range(0 , 10) :
    print("i =",i)
    sum += i
print("sum =",sum)

'''선생님 답안'''

total = 0
for i in range(1, 11) :
    total += i
print("합계 : {}".format(total))


