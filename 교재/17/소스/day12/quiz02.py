import os
# 커피 자판기

money = int(input('요금 입력 : '))

while True :
    print('=========== 커피 자판기 =============')
    print('1. 커피(200)\t2. 코코아(250)\t3. 반환    4. 종료')
    select = int(input('선택> '))

    if select == 4:
        print('프로그램 종료합니다.')
        break
    elif (select == 1 and money < 200) or (select == 2 and money < 250) :
        print('요금이 부족해요')
    elif select == 1 :
        print('맛있게 드세요')
        money -= 200
    elif select == 2 : 
        print('맛있게 드세요')
        money -= 250
    elif select == 3 :
        print('반환 금액 :', money)
        money = 0
    else :
        print('메뉴를 확인 후 다시 입력하세요')
    os.system('pause')
    os.system('cls')
    