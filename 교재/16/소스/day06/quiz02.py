# 입력한 데이터가 3의 배수인 경우 출력하시오.
data = int(input('정수 입력: '))
if data % 3 == 0:
    print('3의 배수입니다.')
if data % 3 != 0:
    print('3의 배수는 아닙니다.')
# 3 % 3, 4 % 3, 5 % 3, 6 % 3

# 수를 입력 받아 짝,홀수를 구분하여 출력하시오.
data = int(input('정수 입력: '))
if data % 2 == 0 :
    print('짝수입니다.')
if data % 2 == 1 :
    print('홀수입니다.')

# 절대값을 구하는 프로그램을 작성하시오.
data = int(input('정수 입력: '))
abs_data = data
# if abs_data < 0 :
#     abs_data = -abs_data
# print('{}의 절대값은 {}입니다.'.format(data, abs_data))
print('{}의 절대값은 {}입니다.'.format(data, abs(abs_data)))

# 두 수를 입력 받아 큰 수를 출력하시오.
data, data2 = input('두 수 입력 : ').split()
data = int(data)
data2 = int(data2)

max_data = data
if max_data < data2 :
    max_data = data2
print('{},{}의 큰 수는 {}입니다.'.format(data, data2, max_data))

# if data > data2 :
#     print('{},{}의 큰 수는 {}입니다.'.format(data, data2, data))

# if data < data2 :
#     print('{},{}의 큰 수는 {}입니다.'.format(data, data2, data2))