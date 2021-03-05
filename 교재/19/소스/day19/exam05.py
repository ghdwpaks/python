def reverse_number(result) :
    tmp = []
    while True :
        tmp.append(result % 10)
        result = result // 10
        if not result :
            break
    return tmp
    

result = int(input('입력 : '))
data1 = reverse_number(result)

data2 = reverse_number(1234)

print(data1)
print(data2)