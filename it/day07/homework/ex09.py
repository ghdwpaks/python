print("Hello world!")

n = int(input("정수 입력 : "))
i1 = int(input("공배수1 입력 : "))
i2 = int(input("공배수2 입력 : "))

if n > 0 :
    if n % i1 == 0 and n % i2 == 0 :
        print("{}는 {},{}의 공배수입니다.".format(n,i1,i2))
else :
    print("{}는 음수입니다.".format(n))
