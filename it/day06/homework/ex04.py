print("Hello world!")

in1 = int(input("숫자 하나 입력해주세요."))

res = in1 > 0 and in1 < 10
print("{}는 1의 자리 숫자가 ".format(in1),end="")
if res :
    print("맞습니다.")
else :
    print("아닙니다.")