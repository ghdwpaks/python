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