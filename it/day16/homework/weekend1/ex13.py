print("sort. 리스트의 값을 오름차순 또는 내림차순으로 정렬한다.")

arr = []

while True :
    u = input("아무 문장 입력 : ")
    if u == 'exit' :
        break
    arr.append(u)
    print("arr :",arr)
print("\n\n입력이 끝났습니다.")
print("\n\n")
print("arr :",arr)

print("\n\n")
arr.sort(reverse=False)
print("오른차순 정렬 후의 arr :",arr)


print("\n\n")
arr.sort(reverse=True)
print("내림차순 정렬 후의 arr :",arr)






