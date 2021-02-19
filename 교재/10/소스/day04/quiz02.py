# 두 수를 입력 받아 합계를 출력하시오.
# data1 = input('입력 : ')
# data2 = input('입력 : ')
# sum_data = int(data1) + int(data2)
# print('data1({}) + data2({})의 합계 : {}'.format(data1, data2, sum_data))

data1, data2 = input('두 수 입력 : ').split() # split() 공백을 기준으로 문자열 분리
sum_data = int(data1) + int(data2)
print('{} + {} = {}'.format(data1, data2, sum_data))