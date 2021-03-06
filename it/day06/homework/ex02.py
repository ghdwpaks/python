print("Hello world!")

in1 = int(input("숫자를 입력해주세요."))

res = in1 > 99 and in1 <1000
print("{}는 3자리수 숫자".format(in1),end="")
if res :
    print("입니다.")
else :
    print("가 아닙니다.")

