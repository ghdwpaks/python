'''
두수를 입력 받아 큰 수를 출력하시오.
'''
print("Hello world!")

in1 = int(input("첫번째 숫자 입력: "))
in2 = int(input("두번째 숫자 입력: "))

if in1 > in2 :
    print("{}이(가) {} 보다 더 큽니다!".format(in1,in2))
elif in1 < in2 :
    print("{}이(가) {} 보다 더 큽니다!".format(in2,in1))

'''선생님 풀이'''

data , data2 = input("두 수 입력 : ").split()
data = int(data)
data2 = int(data2)

if data > data2 :
    print("{},{}의 큰 수는 {}입니다.".format(data,data2,data))


'''선생님 두번째 풀이'''

data , data2 = input("두 수 입력 : ").split()
data = int(data)
data2 = int(data2)
max_data = data
if max_data < data2 :
    max_data = data2
print("{},{}의 큰 수는 {}입니다.".format(data,data2,max_data))





