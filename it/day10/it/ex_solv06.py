'''
1부터 시작하여 홀수의 합을 구하면서
그 합이 10000을 넘지 않는 마지막 수를 구하는
프로그램을 작성하시오
'''

s = 0
i = 0
while s < 10000 :
    s += i
    i += 1 
print(i-1)


'''선생님 답안'''
total = 0
for i in range(1, 300) :
    total += i
    if total >= 10000 :
        break
print("합계 : {}".format(total))




