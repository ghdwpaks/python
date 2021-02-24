import os

stop = True
home = ''
company = ''
while stop :
    print('1.우리집 등록')
    print('2.회사 등록')
    print('3.등록 보기')
    print('4.종료')
    select = int(input('>> '))
    if select == 1 :
        home = input('우리집 등록 : ')
    elif select == 2 :
        company = input('회사 등록 : ')
    elif select == 3 : 
        if home == '' :
            print('집 정보를 입력하세요')
        else :
            print('우리집 : {}'.format(home))
        if company == '' :
            print('회사 정보를 입력하세요')
        else :
            print('회사 : {}'.format(company))
        os.system('pause')
    elif select == 4 :
        stop = False
    else :
        print('메뉴를 확인 후 다시 입력하세요')
    os.system('cls')