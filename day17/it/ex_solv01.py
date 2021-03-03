import copy
m = {}
c = 0
def get_int_input(s) :
    r = 0
    while True:
        try :
            r = input(s)
            if r == 'exit' :
                return 0
            else :
                r = int(r)
                return r
        except :
            print("다시 입력해주세요.")
            continue
        


while True :

    print("====회원 등록 프로그램====")
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
        t = get_int_input("전화번호\t:")
        a = input("주소\t:")
        tmp = {"name" : n,"callnum" : t,"address":a}
        c += 1
        m[c] = copy.deepcopy(tmp)
        tmp.clear()
    elif c == 2 :
        print("출력을 시작합니다.")
        for k,v in m.items() :
            print("m.items() :",m.items())
            print("k :",k)
            print("v :",v)
            print("v.items() : ",v.items())
            for n,t,a in v :
                print("이름 :",n)
                print("전화번호 :",t)
                print("주소 :",a)
    elif c == 3 :
        print("검색을 시작합니다.")
        while True :
            s = get_int_input("검색하시려는 사용자의 번호는?")
            if s in m :
                t = (m.get(s))
                print("이름\t:",t.get("name"))
                print("전화번호\t:",t.get("callnum"))
                print("주소\t:",t.get("address"))
                break
            else :
                print("번호를 다시 입력해주세요.")

    elif c == 4 :
        print("수정을 시작합니다.")

    elif c == 5 :
        print("삭제를 시작합니다.")

    elif c == 6 :
        print("프로그램을 종료합니다.")
    elif c == 0 :
        break







