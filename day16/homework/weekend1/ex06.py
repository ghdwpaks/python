print("extend. 리스트와 리스트를 잇는다.")
arr1 = [10,20,30,40,50]
arr2 = []

while True :
    u = input("아무 문장 입력 : ")
    if u == 'exit' :
        break
    arr2.append(u)
    print("arr2 :",arr2)
print("arr1 :",arr1)
print("arr2 :",arr2)

arr1.extend(arr2)
print("\n\n")
print("arr1 :",arr1)


