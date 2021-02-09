#두 수를 입력받아 사칙연산(+,-,*,/)결과를 출력하시오.

in1 = int(input())
in2 = int(input())
print("{} + {} : {}".format(in1, in2, (in1+in2)))
print("{} - {} : {}".format(in1, in2, (in1-in2)))
print("{} * {} : {}".format(in1, in2, (in1*in2)))
print("{} / {} : {:.2f}".format(in1, in2, (in1/in2)))

'''선생님 풀이'''

data1 = int(input("정수 입력 : "))
data2 = int(input("정수 입력 : "))

sum_data = data1 + data2
sub_data = data1 - data2
mul_data = data1 * data2
div_data = data1 / data2
print("{} + {} = {}".format(data1, data2, sum_data))
print("{} - {} = {}".format(data1, data2, sub_data))
print("{} * {} = {}".format(data1, data2, mul_data))
print("{} / {} = {}".format(data1, data2, div_data))
