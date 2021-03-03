
menu = {}
while True :
    print("1. 메뉴 등록")
    print("2. 메뉴 출력")
    print("3. 메뉴 가격 수정")
    print("4. 메뉴 삭제")
    print("5. 종료")

    print("Menu :" ,menu)
    u = input("작업 선택 : ")
    if u == '1' :
        while True :
            menu_name = input("메뉴 이름 :")
            if menu_name not in menu :
                menu_cost = input("메뉴 가격 :")
            else :
                print("이미 등록된 메뉴입니다.")
            break

        menu[menu_name] = menu_cost


    elif u == '2' :
        '''
        for i in range(0,len(menu)) :
            print(menu[i]['name'] ,":",menu[i]["cost"])
        '''
        print(menu.items())
        for n, c in menu.items() :
            print("{} : {}원".format(n,int(c)))
    elif u == '3' :
        
        while True :
            name = input("수정할 메뉴 이름 :")
            if name in menu :
                price = input("메뉴 가격 :")
                menu[name] = price
                print("메뉴가 수정됐습니다.")
                break
            else :
                print("등록되지 메뉴입니다.")
    elif u == '4' :
        while True :
            name = input("삭제할 메뉴 이름 :")
            if name in menu :
                print("{} : {:,}원".format(name,menu.popitem(name)))
                print("메뉴가 수정됐습니다.")
                break
            else :
                print("등록되지 메뉴입니다.")
    elif u == '5' :
        print("프로그램을 종료합니다.")
        break
