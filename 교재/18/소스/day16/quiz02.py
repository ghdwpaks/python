
# 1. 메뉴 등록
# 2. 메뉴 출력
# 3. 메뉴 가격 수정
# 4. 종료

# 1. 메뉴 등록 : 메뉴이름과 메뉴가격을 입력받아 딕셔너리로 저장한다.
# 2. 메뉴 출력 : 모든 메뉴이름과 가격을 출력한다.
# 3. 메뉴 가격 수정 : 수정할 메뉴 이름을 입력받아 가격을 수정한다.
# 4. 종료 : 반복문을 종료 시킨다.
import os

menu = {}
while True:
    print('1. 메뉴 등록')
    print('2. 메뉴 출력')
    print('3. 메뉴 가격 수정')
    print('4. 메뉴 삭제')
    print('5. 종료')
    try :
        sel = int(input('선택> '))
    except : 
        continue
    if sel == 1 :
        while True :
            name = input('메뉴 이름 : ')
            if name not in menu :
                try :
                    price = int(input('메뉴 가격 : '))
                except :
                    continue
                menu[name] = price
                print('메뉴가 등록되었습니다.')
            else :
                print('등록된 메뉴입니다.')
            break
    elif sel == 2:
        for name, price in menu.items() :
            print('{} : {:,}원'.format(name, price))
    elif sel == 3:
        while True :
            name = input('수정할 메뉴 이름 : ')
            if name in menu : 
                try :
                    price = int(input('메뉴 가격 : '))
                except : 
                    continue
                menu[name] = price
                print('메뉴가 수정되었습니다.')
                break
            else :
                print('수정할 메뉴를 찾을 수 없습니다.')
    elif sel == 4 :
        name = input('삭제할 메뉴 이름 : ')
        if name in menu :
            print('{} : {:,}원'.format(name, menu.pop(name)))
        else :
            print('삭제할 메뉴를 찾을 수 없습니다.')
    elif sel == 5: 
        print('프로그램을 종료합니다.')
        break
    else :
        print('메뉴를 확인 후 다시 입력하세요.')
    os.system('pause')
    os.system('cls')
