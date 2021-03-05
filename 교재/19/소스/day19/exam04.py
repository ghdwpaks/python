def reverse_number(result) :
    tmp = 0
    while True :
        tmp = result % 10
        result = result // 10
        print(tmp, end='')
        if not result :
            break
    print()
    

result = int(input('입력 : '))
reverse_number(result)
print()
reverse_number(1234)