in1 = int(input("숫자입력1 : "))
in2 = int(input("숫자입력2 : "))

print("in1의 2진수 :",bin(in1))
print("in2의 2진수 :",bin(in2))

#or
res = in1 | in2
print("{} | {} = {}".format(bin(in1),bin(in2),res))

#and
res = in1 & in2
print("{} & {} = {}".format(bin(in1),bin(in2),res))

#xor
res = in1 ^ in2
print("{} ^ {} = {}".format(bin(in1),bin(in2),res))



