print("Hello world!")

in1 = int(input("숫자 하나 입력해주세요. >>"))

res = in1 % 2 == 0 and in1 % 3 == 0
print("{}는".format(in1), end="")

if res :
    print("2와 3의 공배수입니다.")
else :
    print("2와 3의 공배수가 아닙니다.")
