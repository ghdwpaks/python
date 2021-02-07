print("Hello world!")

print("계산기를 시작합니다.")
a = b = res = 0
userans1 = ''

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
while(True) :
    print("두번째 숫자를 입력해주세요.\n>>",end='')
    b = input()
    #print(a.isdigit())
    if b.isdigit() :
        b = int(b)
        break
    else :
        print("입력이 잘못됐습니다.\n다시 입력해주세요.")
        continue
print("결과는 " , res , "입니다.")





