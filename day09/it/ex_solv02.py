import os

n = ""
g = [-1,-1,-1]


stop = True
print("Hello world!")
while stop :
    print("="*15)
    print("M E N U".center(15, ' '))
    print("="*15)
    print("1. 학생이름 입력")
    print("2. 성적 3과목 입력")
    print("3. 학생이름 출력")
    print("4. 합계 출력")
    print("5. 평균 출력")
    print("6. 종료")
    print("="*15)

    s = int(input("작업 선택 : "))
    if s == 1 :
        n = input("학생 이름 : ")
    elif s == 2 :
        i = 0
        c = ""
        while i < 3 :
            if i == 0 :
                c = "수학"
            elif i == 1 :
                c = "국어"
            elif i == 2 :
                c = "영어"
            
            while(True) :
                print("{} 점수\n>>".format(c),end='')
                t = input()
                if t.isdigit():
                    if int(t) >= 0 :
                        g[i] = int(t)
                    break
                else :
                    print("입력이 잘못됐습니다.\n다시 입력해주세요.")
                    continue
            i += 1
    elif s == 3 :
        if n == "" :
            print("학생이름을 입력해주시고 와주세요.")
        else :
            print("학생 이름은 {}입니다.".format(n))
            os.system('pause')
    elif s == 4 :
        if g[0] == -1 or g[1] == -1 or g[2] == -1 :
            print("과목점수를 전부 입력하고와주세요.")
        else :    
            print("합계 :",sum(g))
            os.system('pause')
    elif s == 5 :
        if g[0] == -1 or g[1] == -1 or g[2] == -1 :
            print("과목점수를 전부 입력하고와주세요.")
        else :    
            print("평균 :",sum(g)//3)
            os.system('pause')
    elif s == 6 :
        stop = False
    os.system("cls")


'''선생님 답안'''

import os 
stop = True

while stop :
    print("="*20)
    print("{:^20}".format("M e n u"))
    print("="*20)
    print("1. 학생이름 입력")
    print("2. 성적 3과목 입력")
    print("3. 학생이름 출력")
    print("4. 합계 출력")
    print("5. 평균 출력")
    print("6. 종료")
    print("="*20)
    select = int(input(">> "))
    if select == 1 :
        name = input("학생 이름 : ")
    elif select == 2 :
        kor = int(input("국어 점수 입력 : "))
        eng = int(input("영어 점수 입력 : "))
        math = int(input("수학 점수 입력 : "))
        sum = kor + eng + math
        avg = sum / 3
    elif select == 3 :
        if name != '' :
            print("이름 : {} ".format(name))
        else :
            print("이름을 입력 후에 다시 실행하세요.")
        os.system("pause")
    elif select == 4 :
        if sum != "" :
            print("합계 : {}".format(sum))
        else :
            print("3과목의 성적을 입력 후에 다시 실행해주세요.")
    elif select == 5 :
        if sum != "" :
            print("평균 : {:.2f}".format(avg))
        else : 
            print("3과목의 성적을 입력 후에 다시 실행해주세요.")
    elif select == 6 :
        stop = False
    else :
        print("메뉴를 확인 후 다시 입력하세요.")
    os.system('pause')
    os.system('cls')

