# 세 수를 입력 받아 큰 수를 출력 하시오
data1, data2, data3 = input('세 수 입력 : ').split()
data1 = int(data1)
data2 = int(data2)
data3 = int(data3)

max_data = data1
if max_data < data2 :
    max_data = data2
if max_data < data3 :
    max_data = data3
print('{},{},{} 세 수 중 큰 수는 {}입니다.'.format(data1, data2, data3, max_data))

# 두 수를 입력 받아 큰 수가 짝수이면 출력하시오
data1, data2 = input('두 수 입력 : ').split()
data1 = int(data1)
data2 = int(data2)
max_data = data1
if max_data < data2 :
    max_data = data2
if max_data % 2 == 0 :
    print('{},{} 큰 수는 {}이며, 짝수이다.'.format(data1, data2, max_data))
 
#두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오
data1, data2 = input('두 수 입력 : ').split()
data1 = int(data1)
data2 = int(data2)
sum_data = data1 + data2 

if sum_data % 2 == 0 and sum_data % 3 == 0 :
    print('{}는/은 짝수이면서 3의 배수이다.'.format(sum_data))

# if sum_data % 2 == 0 :
#     if sum_data % 3 == 0 :
#           print('{}는/은 짝수이면서 3의 배수이다.'.format(sum_data))