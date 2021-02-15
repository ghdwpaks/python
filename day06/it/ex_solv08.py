'''
두수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오.
'''
print("Hello world!")
in1 = int(input("첫번째 수 입력 : "))
in2 = int(input("두번째 수 입력 : "))

sum1 = in1 + in2
if sum1 % 2 == 0 :
    if sum1 % 3 == 0 :
        print("{}은 합이 짝수이고 3의 배수입니다!".format(sum1))

'''선생님 풀이'''
data1,data2 = input("두 수 입력 : ").split()

data1 = int(data1)
data2 = int(data2)

sum_data = data1 + data2
if sum_data % 2 == 0 and sum_data % 3 == 0 :
    print("{}은(는) 짝수이면서 3의 배수이다.".format(sum_data))









