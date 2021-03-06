import os,copy



info = {}
idx = 0
tmp = {}
while True :
    print("##### 회원 등록 프로그램 #####")
    print("1.등록")
    print("2.출력")
    print("3.검색")
    print("4.수정")
    print("5.삭제")
    print("6.종료")

    sel = int(input("선택 >"))
    if sel == 1 :
        tmp["name"] = input("이름 :")
        tmp["moblie"] = input("전화번호 :")
        tmp["addr"] = input("주소 : ")
        info[idx] = copy.deepcopy(tmp)
        idx += 1
    elif sel == 2:
        for k, v in info.items() :
            print("k :",k)
            print("v :",v)
            print("info.items() : ",info.items())
            print("## {}번째 인적 정보 ##".format(k+1))
            print("v.items() :",v.items())

            for k2, v2 in v.items() :
                print("k2 :",k2)
                print("v2 :",v2)
                print("{} : {}".format(k2,v2))


    elif sel == 3:
        number = int(input("번호 : "))
        if info.get(number) == None :
            print("검색 데이터가 존재하지 않습니다.")
        else :
            print(info.get(number))
        
    elif sel == 4:
        print()
        number = int(input("번호 :"))
        if info.get(number) == None :
            print("수정 데이터가 존재하지 않습니다.")
        else :
            print(info.get(number))
            key = input("수정 항목 :")
            val = input("수정 항목 :")
            info[number][key] = val
            print("수정이 완료되었습니다.")
    elif sel == 5:
        number = int(input("번호 :"))
        if info.get(number) == None :
            print("삭제할 데이터가 존재하지 않습니다.")
        else :
            print(info.pop(number), '삭제 완료')
            print("수정이 완료되었습니다.")
    elif sel == 6:
        print("프로그램을 종료합니다.")
        break
    else : 
        print("메뉴를 확인한 후 다시 입력하세요")
        os.system('pause')
        os.system('cls')



