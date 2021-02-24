#망할 별찍기 : 마름모

line = int(input('출력 행 수 :'))
space = line // 2
star = 1
for i in range(line) :
    for j in range(space) :
        print(" ",end="")
    for i in range(star) :
        print("*",end="")
    print()
    if i < line // 2:
        star += 2
        space -= 1
    else :
        star -=2
        space +=1