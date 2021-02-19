import os

stop = True
name = None
while stop :
    print('1. 이름 입력')
    print('2. 이름 출력')
    print('3. 종료')
    select = int(input('>> '))

    if select == 1 : 
        name = input('이름 입력 : ')
    elif select == 2 :
        if name == None :
            print('이름을 입력 후에 다시 실행하세요')
        else :
            print('이름 : {}'.format(name))
        os.system('pause')
    elif select == 3 :
        stop = False
    else :
        print('메뉴를 확인한 후에 다시 입력하세요')
    os.system('cls') # Linux : clear