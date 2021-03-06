def reverse_number(result) :
    tmp = []
    while True :
        tmp.append(result % 10)
        result = result // 10
        if not result :
            break
    return tmp

result = int(input("입력 : "))
print(reverse_number(result))
print(reverse_number(1234))
restmp = reverse_number(1234)
print(restmp)

