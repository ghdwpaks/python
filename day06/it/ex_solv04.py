'''
절대값을 구하는 프로그램을 작성하시오
'''
print("Hello world!")

in1 = int(input("숫자 입력 : "))

if in1 < 0 :
    in1 = in1 * -1
print("입력하신 숫자의 절댓값은 {}입니다.".format(in1))



'''선생님 풀이'''
data = int(input("정수 입력 : "))

abs_data = data
print("{}의 절댓값은 {}입니다.".format(data, abs(abs_data)))



if abs_data < 0 :
    abs_data = -abs_data
print("{}의 절댓값은 {}입니다.".format(data, abs_data))








