import random
import os
best_score = 0

while True :
    print('== Up & Down Game ==')
    print('1. Game Start')
    print('2. Game Score')
    print('3. Game Exit')
    # 예외 처리 
    try :
        select = int(input('>> '))
    except : 
        continue

    if select == 1 :
        print('<< Game Start >> ')
        com = random.randrange(1, 101)
        print('정답 : ', com)
        count = 0
        while True :
            count += 1
            print('<< Player Turn >> ')
            try :
                player = int(input('Input Number: '))
            except :
                print('정수를 입력을 해주세요')
                continue
            if player < com :
                print('Up!!')
            elif player > com :
                print('Down!!')
            else :
                print('플레이어가 정답을 맞췄습니다!!')
                if best_score > count :
                    best_score = count
                elif best_score == 0:
                    best_score = count
                break
    elif select == 2:
        print('최고 기록은 {}번 입니다.'.format(best_score))
    elif select == 3:
        print('게임을 종료합니다.')
        break
    else : print('메뉴를 확인 후 다시 입력하세요')
    os.system('pause')
    os.system('cls')
    