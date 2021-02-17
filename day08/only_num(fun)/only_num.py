while(True) :
    print("첫번째 숫자를 입력해주세요.\n>>",end='')
    a = input()
    #print(a.isdigit())
    if a.isdigit() :
        a = int(a)
        break
    else :
        print("입력이 잘못됐습니다.\n다시 입력해주세요.")
        continue