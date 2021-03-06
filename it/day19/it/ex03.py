def reverse_number(result) :
    tmp = 0
    while True :
        tmp = result % 10
        result = result // 10
        print("tmp =",tmp)
        if not result :
            print(1)
            break

result = int(input("입력 : "))
print("end1")
print(reverse_number(result))
print("end2")