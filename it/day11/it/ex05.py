#입력된 정수를 거꾸로 출력해주세요

data = int(input("입력 : "))
while True :
    mod = data % 10
    print("{}".format(mod),end="")
    data = data // 10
    if data == 0 :
        break