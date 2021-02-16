data = input("정수 입력 : ")
data = int(data)

if data > 100 :
    print("{}는 100 보다 큰 수 입니다.".format(data))
elif data == 100 :
    print("{}는 100과 같은 수 입니다.".format(data))
elif data > 50 :
    print("{}는 50보다 큰 수 입니다.".format(data))
else :
    print("그 외의 정수입니다.")