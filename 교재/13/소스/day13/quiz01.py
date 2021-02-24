line = 3
space = 2
star = 1
for i in range(line) :
    for j in range(space):
        print(' ',end='')
    for j in range(star) :
        print('*',end='')
    print()
    star += 2
    space -= 1

# 위의 별을 역삼각형으로 찍어주세요
print() 
print()
line = 3
space = 0
star = 5
for i in range(line) :
    for j in range(space):
        print(' ',end='')
    for j in range(star) :
        print('*',end='')
    print()
    star -= 2
    space += 1

line = int(input('별의 출력할 줄 수 입력 : '))
space = line // 2
star = 1
for i in range(line) :
    for j in range(space):
        print(' ',end='')
    for j in range(star) :
        print('*',end='')
    print()
    if i < line // 2:
        star += 2
        space -= 1
    else :
        star -= 2
        space += 1

star = line // 2
space = 1
for i in range(line) :
    for j in range(star) :
        print('*',end='')
    for j in range(space):
        print(' ',end='')
    for j in range(star) :
        print('*',end='')
    print()
    if i < line // 2:
        space += 2
        star -= 1
    else :
        space -= 2
        star += 1