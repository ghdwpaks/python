'''
커피 자판기 만들기
'''

ic = 0 #input cost , 유저가 입력한 요금
ic = int(input("요금을 투입하세요."))
c = ic #while 문이 회전하면서 변화하는 '잔존 금액'

while True :
    print('='*10+"커피 자판기"+'='*10)
    
    print("1. 커피(200)",end="\t")
    print("2. 코코아(250)",end="\t")
    print("3. 반환",end="\t")
    print("4. 종료")
    uin1 = int(input("메뉴를 선택하세요 >>> "))
    if c < 200 :
        uin1 = 4
    if uin1 == 1 :
        print("커피 맛있게 드세요")
        c -= 200
        if c < 0 :
            uin1 = 4
    if uin1 == 2 :
        print("코코아 맛있게 드세요")
        c -= 250
        if c < 0 :
            uin1 = 4
    if uin1 == 3 :
        print("거스름돈 :",c)
        c = 0
    if uin1 == 4 :
        print("프로그램 종료!!!")
        break
'''선생님 답안'''

money = int(input("요금 입력 : "))
while True :
    print("============커피 자판기============")
    print("1.커피(200)\t2. 코코아(250)\t3. 반호나\t4.종료")
    select = int(input("선택 > "))
    if select == 4 :
        print("프로그램 종료합니다.")
        break
    elif (select == 1 and money < 200) or (select == 2 and money < 250) :
        print("요금이 부족해요")
    elif select == 2 :
        print("맛있게 드세요")
        money -= 200
    elif select == 2 :
        print("맛있게 드세요")
        money -= 250
    elif select == 3 :
        print("반환 금액 : ",money)
        money = 0
    else :
        print("메뉴를 확인 후 다시 입력하세요")









