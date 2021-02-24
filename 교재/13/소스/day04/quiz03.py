# 두 수를 입력 받아 사칙연산 (+,-,*,/) 결과를 출력하시오.

# data1 = int(input('정수 입력 : '))
# data2 = int(input('정수 입력 : '))
data1, data2 = map(int, input('두 수 입력: ').split())
sum_data = data1 + data2
sub_data = data1 - data2
mul_data = data1 * data2
div_data = data1 / data2

print('{} + {} = {}'.format(data1, data2, sum_data))
print('{} - {} = {}'.format(data1, data2, sub_data))
print('{} * {} = {}'.format(data1, data2, mul_data))
print('{} / {} = {}'.format(data1, data2, div_data))