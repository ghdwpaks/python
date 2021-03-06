

loop_flag = True

while loop_flag :
    data = input("입력 : ")
    print("입력 데이터는 '{}'입니다.".format(data))
    if data == "종료" :
        break

loop_count = int(input("반복 횟수 : "))
i = 1
while i <= loop_count :
    print("{}번째 반복".format(i))
    i += 1