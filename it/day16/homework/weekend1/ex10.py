print("count. 배열에서 일치하는 값의 갯수를 반환한다.")

arr = []

while True :
    u = input("아무 문장 입력 : ")
    if u == 'exit' :
        break
    arr.append(u)
    print("arr :",arr)
print("\n\n입력이 끝났습니다.")
print("arr :",arr)

c = 0
for i in range(0,len(arr)) :
    for j in range(0,len(arr[i])) :
        tmp = arr[i][j]
        if tmp == 'a' or tmp == 'A' :
            c += 1
print("arr안에 a 는 {}개가 있습니다!".format(c))

c = 0
for i in range(0,len(arr)) :
    c += arr[i].count('a')
    c += arr[i].count('A')
print("arr안에 a 는 {}개가 있습니다!".format(c))