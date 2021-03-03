# 세 수 중 최대/최소 값을 구하는 프로그램 작성
data1, data2, data3 = input('세 수 입력 : ').split()
data1 = int(data1)
data2 = int(data2)
data3 = int(data3)

max_data = data1
min_data = data2
if data1 < data2 :
    max_data = data2
    min_data = data1

if max_data < data3 :
    max_data = data3
elif min_data > data3 :
    min_data = data3

print('{},{},{} 수 중에 최댓값 {}, 최솟값 {} 입니다.'.format(data1, data2, data3, max_data, min_data))

# 1) 3의배수이면서,4의배수에도 해당 => [ ]은(는)3의 배수이면서,4의 배수입니다.
# 2) 3의배수에만 해당 => [ ]은(는)3의 배수입니다.
# 3) 4의배수에만 해당 => [ ]은(는)4의 배수입니다.
# 4) 3의배수도,4의배수도 해당안됨 => [ ]은(는)3의배수도 4의배수도 아닙니다.
# 5) ( 0 입력시 잘못입력)
data = int(input('정수 입력 : '))

print_data = ''
if data == 0 :
    print_data = '{}은(는) 잘 못 입력'.format(data)
elif data % 3 == 0 and data % 4 == 0 :
    print_data = '{}은(는) 3의 배수이면서, 4의 배수 입니다.'.format(data)
elif data % 3 == 0 :
    print_data = '{}은(는) 3의 배수 입니다.'.format(data)
elif data % 4 == 0 :
    print_data = '{}은(는) 4의 배수 입니다.'.format(data)
else :
    print_data = '{}은(는) 3의 배수도 4의 배수도 아닙니다.'.format(data)

print(print_data)