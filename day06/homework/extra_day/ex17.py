in1 = int(input("숫자입력 : "))


result = in1 << 4
print("{} << 4 = {}".format(in1,result))

in1 <<= 4
result = in1 >> 2
print("{} >> 2 = {}".format(in1 , result))

result = ~in1
print("~{} = {}".format(in1,result))
