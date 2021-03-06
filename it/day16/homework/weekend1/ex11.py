print("index는 리스트에서 일치하는 값의 인덱스 번호를 반환합니다.\n")

arr = []
for i in range(1,6) :
    for j in range(0,i) :
        arr.append(i*10)
print("arr :",arr)


print(arr.index(10))
print(arr.index(20))
print(arr.index(30))
print(arr.index(40))
print(arr.index(50))





