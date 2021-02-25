import random
import os
print("Hello world!")


print("Hello world!")

def get_int(s) :
    while(True) :
        print("{}\n>>".format(s),end='')
        a = input()
        #print(a.isdigit())
        if a.isdigit() :
            a = int(a)
            return a
        else :
            print("입력이 잘못됐습니다.\n다시 입력해주세요.")
            continue

def get_y_or_n(s) :
    while(True) :
        print("{}\n>>".format(s),end='')
        a = input()
        if a == 'yes' or a == "y"  or a == "yeah"  or a == "예"  or a == "ㅖ"  or a == "네"  or a == "ㅇ"  or a == "ㅇㅇ"  or a == "P"  or a == "p"  or a == "dP"  or a == "sp"  or a == "d"  or a == "dd" :
            return True
        if a == "n"  or a == "no"  or a == "nope"  or a == "아니"  or a == "ㄴㄴ"  or a == "ㄴ"  or a == "ㅜ"  or a == "ㅜㅐ"  or a == "dksldy"  or a == "dksl"  or a == "ss"  or a == "s":
            return False


p = True
c = 10000
while p :
    print("=== DICE Game ===")
    print("1. Game Start")
    print("2. left cost")
    print("3. Exit Game")
    #print("현재 배팅 가능 금액은 {}원 입니다.".format(c))
    u = get_int("입력 :")
    
    if u == 3 :
        os.system("cls")
        print("게임을 종료합니다.")
        p = False
    elif c <= 0 :
        os.system("cls")
        print("배팅 가능 금액이 없습니다.") 
    elif u == 1:
        
        p2 = True
        while p2 :
            
            os.system("cls")
            us = 0
            for i in range(1,4) :
                s = random.randrange(1,7)
                print("{}번째 주사위 : {}".format(i,s))
                us += s
            print("당신의 주사위 총 합 :",us)
            p3 = True
            gc = 0
            while p3 :
                gc = get_int("배팅 금액을 정해주세요.")
                if gc > c :
                    print("다시 입력해주세요.")
                else :
                    c -= gc
                    p3 = False
            
            com = random.randrange(1 , 19)
            print("당신의 눈 :",us)
            print("상대의 눈 :",com)
            if us > com :
                print("이겼습니다! {}을 얻었습니다.".format(gc))
                c += gc * 2
            else :
                print("졌습니다. {}을 잃었습니다.".format(gc))
            os.system("pause")
            if c > 0 :
                p2 = get_y_or_n("계속해서 게임을 계속하시겠습니까? (Y / N)")
            elif c <= 0 :
                p2 = False
    elif u == 2 :
        os.system("cls")
        print("현재 배팅 가능 금액은 {}원이 남았습니다.".format(c))
        os.system("pause")

    elif u == 3 :
        os.system("cls")
        print("게임을 종료합니다.")
        p = False



