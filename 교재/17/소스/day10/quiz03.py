# 1부터 시작하여 홀수의 합을 구하면서
# 그 합이 10000을 넘지 않는 마지막 수를 구하는 
# 프로그램을 작성하시오.
total = 0
for i in range(1, 300, 2) :
    total += i
    if total >= 10000 :
        break
print('합계 : {}, 마지막 홀수 : {}'.format(total, i))


# 수를 입력 받아 소수인지 아닌지 판별해서 출력하세요.
# 소수 : 2, 3, 5, 7, 11, 13 

# 11 % 2 == 0
# 11 % 3 == 0
# 11 % 4 == 0
# 11 % 5 == 0
# 11 % 6 == 0
# 11 % 7 == 0
# 11 % 8 == 0
# 11 % 9 == 0
# 11 % 10 == 0

data = int(input('입력 : '))
print_string = "소수입니다."

for i in range(2, data) : 
    if data % i == 0 :
        print_string = "소수가 아닙니다."

print('{}는/은 {}'.format(data, print_string))