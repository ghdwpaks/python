import random
import os

count = win = draw = lose = 0
money = 10000
while True :
    print("=== Dice Game ===")
    print("1. Game Start")
    print("2. left cost")
    print("3. Exit Game")
    try :
        select = int(input(">> "))
    except :
        os.system("cls")
        continue
    if select == 1 :
        print("게임을 시작합니다.")
        while True :
            com = user = 0
            if money <= 0 :
                print("베팅 금액을 모두 잃었습니다. 종료합니다.")
                break
            count += 1
            print("배팅 금액 :",money)

            print("주사위를 돌리겠습니다.")
            for i in range(1,4) :
                tmp = random.randrange(1,7)
                user += tmp
                print("{}번째 주사위 : {}".format(i,tmp))
            print("당신의 주사위 총 합 :",user)
            for i in range(1,4) :
                tmp = random.randrange(1,7)
                com += tmp
            while True :
                try :
                    bat = int(input("배팅 금액을 정해주세요 : "))
                except :
                    continue
                if bat >= 1000 and bat <= money :
                    break
            print("=== 결과 ===")
            print("당신의 눈 :",user)
            print("상대의 눈 :",com)

            if com == user :
                print("무승부입니다.")
                draw += 1
            elif com > user :
                print("졌습니다. {}원을 잃었습니다.".format(bat))
                lose += 1
            ans = input("계속 하시겠습니까? ( Y / N )")
            if ans == 'y' or ans == 'Y' :
                continue
            else :
                break



    elif select == 2 :
        print("현재 {}전 {}승 {}무 {}패 입니다.".format(count, win, draw,lose))
    elif select == 3:
        print("게임을 종료합니다.")
        break
    else :
        print("메뉴를 확인 후 다시 입력하세요.")





