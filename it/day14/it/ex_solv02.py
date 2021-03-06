'''
동전 앞/뒤 맞추는 게임

'''
import random

print("Hello world!")
p = True
while p :
    print("== 동전 앞/뒤 맞추기 ==")
    print("1.앞면/2.뒷면/3.종료")
    u = int(input("선택 > "))
    i = int(random.randrange(1,3))
    if u == 3 :
        print("종료합니다.")
        break
    elif u == i :
        print("맞췄습니다!")
    else :
        print("틀렸습니다!") 


'''선생님 답안'''
import random
import os
while True :
    print("== 동전 앞/뒤 맞추기 ==")
    print("1.앞면/2.뒷면/3.종료")
    select = int(input("선택 > "))
    com = random.randrange(1,3)
    if select == 3 :
        print("동전 게임을 종료합니다")
        break
    if 0 < select and select < 3 :
        if com == select :
            print("맞췄습니다!")
        else :
            print("틀렸습니다.")
    else :
        print("메뉴를 확인 후 다시 입력해주세요.")
    os.system("pause")
    os.system("cls")
    
