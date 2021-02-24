

# 1 ~ 10까지의 합계를 구해주세요.

# total = 1 + 2+3+4+5+6+7+8+9+10
# print(total)
#range(1, 11) 1~10
total = 0
for i in range(1, 11) :
    total = total + i # 첫번째는 1
print("합계 : {}".format(total))

# 아래와 같이 출력 하시오
#  1 	  2 	  3 	  4 	 5 
#  6 	  7 	  8 	  9 	 10 	 
# 11 	 12 	 13 	 14 	 15 	 
# 16 	 17 	 18 	 19 	 20 	 
# 21 	 22 	 23 	 24 	 25 	 
# 26 	 27 	 28 	 29 	 30 

for i in range(1, 31) :
    print('{}'.format(i), end='\t')
    if i % 5 == 0:
        print()

#정수를 입력 받아 1 ~ 입력 받은 정수까지 합을 구하시오.
data = int(input('정수 입력 : '))
data += 1
total = 0
for i in range(1, data) :
    total += i
print('합계 : {}'.format(total))

#정수를 입력 받아 1 ~ 입력 받은 정수까지 
#짝수 합과 홀수 합을 구하시오.
data = int(input('정수 입력 : '))
data += 1
odd_total = 0
even_total = 0
for i in range(1, data) :
    if i % 2 == 0 :
        even_total += i
    else :
        odd_total += i

print('짝수 합계 : {}'.format(even_total))
print('홀수 합계 : {}'.format(odd_total))