'''
1에서 1000까지의 자연수중에서 4로 나누어도 6으로 나누어도 나머지가 1인 수의 합을 출력하라.
'''

s = 0 
for i in range(1, 1001) :
    if i % 4 == 1 and i % 6 == 1 :
        s += i
print("합계 :",s)


'''선생님 답안'''
total = 0
for i in range(1 , 1001) :
    if i % 4 == 1 and i % 6 == 1 :
        total += i
print("합 : {}".format(total))



