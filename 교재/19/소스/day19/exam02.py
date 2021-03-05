result, tmp = 0, 0
result = int(input('입력 : '))
while True :
    tmp = result % 10
    result = result // 10
    print(tmp, end='')
    if not result :
        break
print()