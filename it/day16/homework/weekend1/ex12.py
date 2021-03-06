print("reverse는 리스트의 모든 값을 뒤집어 나열합니다.")

arr = []

while True :
    u = input("아무 문장 입력 : ")
    if u == 'exit' :
        break
    arr.append(u)
    print("arr :",arr)
print("\n\n입력이 끝났습니다.")
print("reverse 전의 arr :",arr)
arr.reverse()
print("reverse 후의 arr :",arr)

