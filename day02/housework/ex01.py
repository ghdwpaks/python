print("a\n>>" ,end='')
a = int(input())
#input함수는 기본적으로 입력받는 모든것을 문자열취급한다.
print("a :",a)


print("b\n>>", end='')
b = input()
print("a :",a)
b = int(b)
print("a+b = ", a+b)
print("\n분기점\n")
c = a+b
print("c : ", c)
print("\n분기점\n")
a = int(a)
print("a :" ,a)
b = int(b)
print("b : ", b)
print("a+b : ",a+b)