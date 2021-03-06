print("Hello world!")

arr = []
lim = 0

while(True) :
    print("수 몇개를 정렬하시겠습니까?\n>>",end='')
    lim = input()
    if lim.isdigit() :
        lim = int(lim)
        break
    else :
        print("입력이 잘못됐습니다.\n다시 입력해주세요.")
        continue


i = 0
while i < lim :
    while(True) :
        print("입력할 수\n>>",end='')
        e = input()
        if e.isdigit() :
            e = int(e)
            arr.append(e)
            #print(arr[i])
            break
        else :
            print("입력이 잘못됐습니다.\n다시 입력해주세요.")
            continue
    i += 1
    #print("arr = {}".format(arr))
arr.sort()
#print("at input end : arr = {}".format(arr))
print("\n\n입력하신 수는 ",end='')
i = 0
while i < lim :
    print("{}".format(arr[i]),end="")
    if not i == (lim - 1) :
        print(' , ',end="")
    i += 1
print("이 있으며")
print("가장 큰 수는 {}입니다.".format(arr[lim - 1]))

