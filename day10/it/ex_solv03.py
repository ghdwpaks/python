'''
정수를 입력 받아 1 ~ 입력 받은 정수까지
짝수 합과 홀수 합을 구하시오.

'''
l = int(input("정수 입력"))
ev = 0 #짝수
od = 0 #홀수

for i in range(1 , l) :
    if i % 2 == 0 :
        #짝수
        #print("짝 :",i)
        ev += i
    else :
        #홀수
        #print("홀 :",i)
        od += i
print("짝수 총합 :",ev)
print("홀수 총합 :",od)


'''선생님 답안'''

data = int(input("정수 입력 : "))
data += 1
odd_total = 0
even_total = 0
for i in range(1,data) :
    if i % 2 == 0 :
        even_total += i
    else :
        odd_total += i
print("짝수 합계 : {}".format(even_total))
print("홀수 합계 : {}".format(odd_total))



