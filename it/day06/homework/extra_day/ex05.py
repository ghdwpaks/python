print("Hello world!")

in1 = 0b10
#2진수 변수설정. 0b뒤에 있는 숫자는 2진수로 인식한다.
print("in1 = {}".format(in1))


in2 = 0o10
#8진수 변수설정. 0o뒤에 잇는 숫자는 8진수로 인식한다.
print("in2 = {}".format(in2))


in3 = 0x10
#16진수 변수설정. 0o뒤에 잇는 숫자는 16진수로 인식한다.
print("in3 = {}".format(in3))

in4 = 10
in5 = 100

print()
print("in{} {}진수 출력 : {}".format(1,2,bin(in1)))
print("in{} {}진수 출력 : {}".format(2,2,bin(in2)))
print("in{} {}진수 출력 : {}".format(3,2,bin(in3)))
print("in{} {}진수 출력 : {}".format(4,2,bin(in4)))
print("in{} {}진수 출력 : {}".format(5,2,bin(in5)))

print()
print("in{} {}진수 출력 : {}".format(1,8,oct(in1)))
print("in{} {}진수 출력 : {}".format(2,8,oct(in2)))
print("in{} {}진수 출력 : {}".format(3,8,oct(in3)))
print("in{} {}진수 출력 : {}".format(4,8,oct(in4)))
print("in{} {}진수 출력 : {}".format(5,8,oct(in5)))

print()
print("in{} {}진수 출력 : {}".format(1,16,hex(in1)))
print("in{} {}진수 출력 : {}".format(2,16,hex(in2)))
print("in{} {}진수 출력 : {}".format(3,16,hex(in3)))
print("in{} {}진수 출력 : {}".format(4,16,hex(in4)))
print("in{} {}진수 출력 : {}".format(5,16,hex(in5)))