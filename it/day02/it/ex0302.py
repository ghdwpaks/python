num2 = 0b100
print("num2 : " ,num2)
#다만 2진수의 입력은 조금 다른게, 0과 1 이외의 상수는 입력되지 않는다.

num8 = 0x100
print("num8 : ", num8)

num16 = 0o100
print("num16 : ", num16)

#이렇게 0x, 0o를 붙혀서 작성한다고 해도 출력할때는 10진수로써 출력된다.
#만약에 10진수로써 출력하기 싫다고 한다면 아래같이 하면 된다.

print()
#일반변수 및 상수를 2진수로 출력
print("num2 2진수 출력 :" , bin(num2))
print("num8 2진수 출력 :" , bin(num8))
print("num16 2진수 출력 :" , bin(num16))
print()

#일반변수 및 상수를 16진수로 출력
print("num2 8진수 출력 : ",oct(num2))
print("num8 8진수 출력 : ",oct(num8))
print("num16 8진수 출력 : ",oct(num16))
print()

#일반변수 및 상수를 16진수로 출력
print("num2 16진수 출력 : ",hex(num2))
print("num8 16진수 출력 : ",hex(num8))
print("num16 16진수 출력 : ",hex(num16))
print()

