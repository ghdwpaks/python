'''
=== Dice Game ===
1. Game Start
2. Game Score
3. End Game
>> 1
게임을 시작합니다.
계속하려면 아무 키나 누르십시오 . . .

배팅 금액: 10000
주사위를 돌리겠습니다.
1번째 주사위 : 6
2번째 주사위 : 4
3번째 주사위 : 4
당신의 주사위 총 합: 14
배팅 금액을 정해주세요 : 10000
=== 결과 ===
당신의 눈 : 14
상대의 눈 : 6
이겼습니다. 10000원을 얻었습니다.
게임을 계속하시겠습니까? (y/n) : y

배팅 금액: 160000
주사위를 돌리겠습니다.
1번째 주사위 : 2
2번째 주사위 : 1
3번째 주사위 : 5
당신의 주사위 총 합: 8
배팅 금액을 정해주세요 : 160000
=== 결과 ===
당신의 눈 : 8
상대의 눈 : 9
졌습니다. 160000원을 잃습니다.
게임을 계속하시겠습니까? (y/n) : y

배팅금액을 모두 잃었습니다. 종료합니다.
계속하려면 아무 키나 누르십시오 . . .

=== Dice Game ===
1. Game Start
2. Game Score
3. End Game
>> 2
현재  5전 4승 0무 1패 입니다.
계속하려면 아무 키나 누르십시오 . . .

'''



import random
import os

count = win = draw = lose = 0
money = 10000

while True :
    print('=== Dice Game ===')
    print('1. Game Start')
    print('2. Game Score')
    print('3. End Game')
    try :
        select = int(input('>> '))
    except :
        os.system('cls')
        continue

    if select == 1 :
        print('게임을 시작합니다.')
        while True :
            if money <= 0 :
                print('배팅 금액을 모두 잃었습니다. 종료합니다.')
                break
            
            count += 1
            print('배팅 금액 : ', money)

            user = 0
            print('주사위를 돌리겠습니다.')
            for i in range(1, 4) : 
                tmp = random.randrange(1, 7)
                user += tmp
                print('{}번째 주사위 : {}'.format(i, tmp))
            print('당신의 주사위 총 합 : ', user)

            com = 0
            for i in range(3) : 
                tmp = random.randrange(1, 7) 
                com += tmp

            while True :
                try : 
                    bat = int(input('배팅 금액을 정해주세요 : '))
                except :
                    continue
                if bat >= 1 and bat <= money :
                    break
            
            print('=== 결과 ===')
            print('당신의 눈 : ', user)
            print('상대의 눈 : ', com)

            if com == user :
                print('무승부입니다.')
                draw += 1
            elif com > user :
                print('졌습니다. {}원을 잃었습니다.'.format(bat))
                lose += 1
                money -= bat
            else :
                print('이겼습니다. {}원을 얻었습니다.'.format(bat))
                win += 1
                money += bat
                
            while True :
                yn = input('게임을 계속하시겠습니까? (y/n) : ')
                if yn == 'y' or yn == 'n' or yn == 'Y' or yn == 'N' :
                    break
                print('입력 값은 y/n 입니다.')

            if yn == 'n' or yn == 'N' :
                print('게임을 종료합니다.')
                break
    elif select == 2:
        print('현재 {}전 {}승 {}무 {}패 입니다.'.format(count, win, draw, lose))
    elif select == 3: 
        print('게임을 종료합니다.')
        break
    else : print('메뉴를 확인 후 다시 입력하세요.')

    os.system('pause')
    os.system('cls')