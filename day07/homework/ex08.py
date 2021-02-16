print("Hello world!")

in1 = int(input("정수 입력 : "))

res = 0
i = 0
tin1 = in1
print("tin1 = ",tin1)
while tin1 > 10 :
    tin1 = tin1 // 10
    res += 1


print("res =",res)

print("{}는 ".format(in1),end="")

if res == 1 :
    print("10",end="")
elif res == 2 :
    print("100",end="")
elif res == 3 :
    print("1000",end="")
else :
    print("측정불가")
print("자리의 수 입니다!")
print("\n\n분기점\n\n")

print("{}는 {}의 자리 숫자입니다!".format(in1, 10 ** res))






