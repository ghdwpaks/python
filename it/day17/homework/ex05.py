import copy
m = []
c = 0
def get_int_input(s) :
    r = 0
    while True:
        try :
            r = input(s)
            if r == 'exit' :
                return 0
            elif r.isdigit():
                r = int(r)
                return r
            else :
                continue
        except :
            print("다시 입력해주세요.")
            continue
        

count = 0
while True :

    print("====회원 등록 프로그램====")
    print("count =",count)
    print("1. 등록")
    print("2. 출력")
    print("3. 검색")
    print("4. 수정")
    print("5. 삭제")
    print("6. 종료")
    c = get_int_input("작업 선택 : ")#choice
    if c == 1 :
        print("등록을 시작합니다.")
        n = input("이름\t:")
        t = get_int_input("전화번호:")
        a = input("주소\t:")
        tmp = {"name" : n,"callnum" : t,"address":a}
        count += 1
        m.append(tmp)
        print("m :",m)
    elif c == 2 :
        print("출력을 시작합니다.")
        print(m)
        #print(m.items())
        for i in range(0,len(m)) :
            '''
            n = v["name"]
            t = v["callnum"]
            a = v["address"]
            '''
            print("{}번째 유저 데이터 :".format(i))
            print("이름\t:",m[i]["name"])
            print("전화번호:",m[i]["callnum"])
            print("주소\t:",m[i]["address"])
            print("\n")



            '''
            print("m.items() :",m.items())
            print("k :",k)
            print("v :",v)
            print("v.items() : ",v.items())
            print("v[1] : ",v["name"])
            '''


            '''
            for n,t,a in v :
                print("이름 :",n)
                print("전화번호 :",t)
                print("주소 :",a)
            '''
            #이거 위에 박스 각주 친 곳 왜 안돼는지 모르겠음

    elif c == 3 :
        print("검색을 시작합니다.")
        while True :
            s = get_int_input("검색하시려는 사용자의 번호는?")
            if s == 0 : break
            elif not(m[s] == None) :
                print("이름\t:",m[s]["name"])
                print("전화번호:",m[s]["callnum"])
                print("주소\t:",m[s]["address"])
                break
            else :
                print("번호를 다시 입력해주세요.")

    elif c == 4 :
        print("수정을 시작합니다.")
        while True :
            s = get_int_input("수정하시려는 사용자의 번호는?")
            if s == 0 : break
            elif not(m[s] == None) :
                print("{}번째 유저 데이터 :".format(s))
                print("이름\t:",m[s]["name"])
                print("전화번호:",m[s]["callnum"])
                print("주소\t:",m[s]["address"])
                print("\n")

                n = input("이름\t:")
                t = get_int_input("전화번호:")
                a = input("주소\t:")
                tmp = {"name" : n,"callnum" : t,"address":a}
                count += 1
                m[s] = tmp
                print("수정이 완료됐습니다!")
                print("m :",m)
                
                break
            else :
                print("번호를 다시 입력해주세요.")

    elif c == 5 :
        print("삭제를 시작합니다.")
        while True :
            s = get_int_input("수정하시려는 사용자의 번호는?")
            if s == 0 : break
            elif not(m[s] == None) :
                m[s]["name"] = None
                m[s]["callnum"] = None
                m[s]["address"] = None
                print("삭제됐습니다!")
                break
            else :
                print("번호를 다시 입력해주세요.")
    elif c == 6 :
        print("프로그램을 종료합니다.")
    elif c == 0 :
        break







