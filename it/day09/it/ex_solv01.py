print("Hello world!")
import os

home = None
com = None
while True :
    print("1.우리집 등록")
    print("2.회사 등록")
    print("3.등록 보기")

    in1 = int(input("작업 선택 : "))
    if in1 == 1 :
        home = input("집 위치 : ")
    elif in1 == 2:
        com = input("회사 위치 : ")
    elif in1 == 3:
        if home == None :
            print("집을 먼저 등록해주세요.") 
        elif com == None :
            print("회사를 먼저 등록해주세요.")
        else :
            print("우리집 : {}\n회사 : {}".format(home,com))
            os.system('pause')
    else :
        print("메뉴를 다시 봐주세요.")
    os.system("cls")

'''선생님 풀이'''
stop = True
home = ""
company = ''


while stop :
    print("1.우리집 등록")
    print("2.회사 등록")
    print("3.등록 보기")
    print("4.종료")
    select = int(input(">> "))
    if select == 1 :
        home = input("우리집 등록 : ")
    elif select == 2 :
        company = input("회사 등록 : ")
    elif select == 3 :
        if home == '':
            print("집 정보를 입력하세요")
        else :
            print("우리집 : {}".format(home))
        if company == '' :
            print("회사 정보를 입력하세요")
        else :
            print("회사 : {}".format(company))
        os.system("pause")
    elif select == 4 :
        stop = False
    else :
        print("메뉴를 확인 후 다시 입력하세요.")
    os.system("cls")








