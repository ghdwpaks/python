#업 앤 다운 게임 만들기
import random
print("Hello world!")
c = 100
p1 = True
while p1 :
    i = random.randrange(1,101)
    print("== Up & Down Game ==")
    print("1. Game Start")
    print("2. Game Score")
    print("3. Game Exit")
    u = 0
    while(True) :
        print(">",end='')
        u = input()
        if u.isdigit() :
            u = int(u)
            break
        else :
            print("입력이 잘못됐습니다.\n다시 입력해주세요.")
            continue
    uc = 0
    if u == 1 :
        uc += 1
        print("<< Game Start >>")
        print("정답 :",i)
        ug = 0
        p2 = True
        while p2 :
            uc += 1
            while True :
                print(">",end='')
                ug = input()
                if ug.isdigit() :
                    ug = int(ug)
                    break
                else :
                    print("입력이 잘못됐습니다.\n다시 입력해주세요.")
                    continue
            if ug > i :
                print("Down!!")
            elif ug < i :
                print("Up!!")
            elif ug == i :
                p2 = False
        print("플레이어가 정답을 맞췄습니다!")
        if c > uc :
            c = uc
    elif u == 2 :
        if c == 100 :
            print("아직 기록이 세워지지 않았습니다!")
        else :
            print("현재 최단 {}번으로 정답을 맞췄습니다!".format(c))
    elif u == 3 :
        print("프로그램을 종료합니다.")
        break
    print("\n\n\n")


import random
import os

best_score = 100
while True :
    print("== Up & Down Game ==")
    print("1. Game Start")
    print("2. Game Score")
    print("3. Game Exit")
    try :
        select = int(input(">> "))
    except :
        continue

    if select == 1 :
        print("<< Game Start >>")
        com = random.randrange(1,101)
        print("정답 :",com)
        count = 0
        while True :
            count += 1
            print("<< Player Turn >>")
            try :
                player = int(input("Input Number :"))
            except :
                print("정수를 입력해주세요")
                continue
            if player < com :
                print("up!!")
            elif player > com :
                print("Down!!")
            else :
                print("플레이어가 정답을 맞췄습니다!!!")
                if best_score > count :
                    best_score = count
                break
            print("Up!!")
    elif select == 2 :
        print("최고 기록은 {}번 입니다.".format(best_score))
    elif select == 3:
        print("게임을 종료합니다.")
        break
    else :
        print("메뉴를 확인 후 다시 입력하세요")
    os.system("pause")
    os.system("cls")


