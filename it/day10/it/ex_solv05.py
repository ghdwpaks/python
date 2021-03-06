'''
두 수를 입력 받아 작은 수 ~ 큰 수의 합계를 출력하세요.
'''

s = int(input("정수입력1 : "))
e = int(input("정수입력1 : "))
sum = 0
for i in range(s , e) :
    sum += i
print(sum)


'''선생님 답안'''
data1, data2 = input("두 수 입력 : ").split()
data1 = int(data1)
data2 = int(data2)
if data1 > data2 :
    tmp = data1
    data1 = data2
    data2 = tmp


total = 0
for i in range(data1, data2+1) :
    total += i
print("{} ~ {}의 합계 : {}".format(data1,data2,total))



