'''
두 수를 입력 받아 큰 수가 짝수이면 출력하시오
'''
print("Hello world!")
in1 = int(input("첫번째 수 입력 : "))
in2 = int(input("두번째 수 입력 : "))

max_int = in1
if max_int < in2 :
    max_int = in2

if max_int % 2 == 0 :
    print("큰 수는 {} 이며, 짝수입니다!".format(max_int))



'''선생님 풀이'''
data1, data2 = input("두 수 입력 : ").split()

data1 = int(data1)
data2 = int(data2)
max_data = data1
if max_data < data2 :
    max_data < data2
if max_data % 2 == 0 :
    print("{}와{}중 큰 수는 {}이며, 짝수이다.".format(data1,data2,max_data))











