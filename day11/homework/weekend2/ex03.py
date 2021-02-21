print("Hello world!")
import csv
import os
n1_object = 0 #하드난이도인지 아닌지 맞으면 1, 아니면 0.
n2_object = 0 #목표물이 뭔지
dis_gunner = 0 #총잡이 지분 %
dis_driver = 0 #운전사 지분 %
dis_hack = 0 #해커 지분 %
add_cost = 0 #보조작업 구매로 인해 붙는 추가금액
user_share = 0 #플레이어의 지분 %
result = 0 #플레이어의 실제 수익 결과 ($)
object_cost = 0 #목표 그 자체의 수익금
p = True

object_list = []
with open('data_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        object_list.append(row)
print("object_list =",object_list)

def only_number(n,s) :
    n = int(n)
    while(True) :
        print("{} >>".format(s),end='')
        n = input()
        #print(a.isdigit())
        if n.isdigit() :
            n = int(n)
            break
        else :
            print("숫자로 다시 입력해주세요.")
            continue
    return n

def check_difficult() :
    in1 = input("난이도는 어려움(하드, 해골)난이도 인가요? (1/0)\n>>")
    global n1_object
    if in1 == "1" or in1 == "네" or in1 == "예" or in1 == "ㅖ" or in1 == "P" or in1 == "p" or in1 == "응" or in1 == "어" or in1 == "맞아" or in1 == "yes" or in1 == "YES" or in1 == "y" or in1 == "yeah" or in1 == "ㅇ" or in1 == "Y" :
        print("난이도는 어려움입니다.")
        n1_object = 1
    elif in1 == "0" or in1 == "아니" or in1 == "ㄴ" or in1 == "아님" or in1 == "아니야" or in1 == "아닙니다" or in1 == "n" or in1 == "N" or in1 == "nope" or in1 == "no" or in1 == "NO" or in1 == "ㄴㄴ" or in1 == "아니요" :
        print("난이도는 보통입니다.")
        n1_object = 0


def select_team() :
    #print("총잡이, 운전사, 해커의 지분을 결정하는 함수에 진입했습니다.")

    os.system('cls')
    print("총잡이는 누구로 선택하시겠습니까?")

    print("1.[초보자]\t칼 아볼라지")
    print("2.[중급자]\t찰리 리드")
    print("3.[전문가]\t패트릭 맥리어리")
    print("4.[전문가]\t구스타보 모타 ")
    print("5.[전문가]\t체스터 맥코이")
    print()
    in_gun = 0
    in_gun = only_number(in_gun,"총잡이")
    global dis_gunner
    if in_gun == 1 :
        dis_gunner = 5
    elif in_gun == 2 :
        dis_gunner = 7
    elif in_gun == 3 :
        dis_gunner = 8
    elif in_gun == 4 :
        dis_gunner = 9 
    elif in_gun == 5 :
        dis_gunner = 10
    print("\n\n")





    os.system('cls')
    print("운전사는 누구로 선택하시겠습니까?")

    print("1.[초보자]\t카림 덴즈")
    print("2.[중급자]\t자크 넬슨")
    print("3.[중급자]\t탈리아나 마르티네즈")
    print("4.[전문가]\t에디 토")
    print("5.[전문가]\t체스터 맥코이")
    print()
    in_driver = 0
    in_driver = only_number(in_driver,"운전사")
    global dis_driver
    if in_driver == 1 :
        dis_driver = 5
    elif in_driver == 2 :
        dis_driver = 6
    elif in_driver == 3 :
        dis_driver = 7
    elif in_driver == 4 :
        dis_driver = 9 
    elif in_driver == 5 :
        dis_driver = 10
    print("\n\n")






    os.system('cls')
    print("해커는 누구로 선택하시겠습니까?")

    print("1.[초보자]\t리키 루켄스")
    print("2.[중급자]\t요한 블레어")
    print("3.[중급자]\t크리스티안 펠츠")
    print("4.[전문가]\t페이지 해리스")
    print("5.[전문가]\t에비 슈왈츠먼")
    print()
    in_hack = 0
    in_hack = only_number(in_hack,"해커")
    global dis_hack
    if in_hack == 1 :
        dis_hack = 3
    elif in_hack == 2 :
        dis_hack = 5
    elif in_hack == 3 :
        dis_hack = 7
    elif in_hack == 4 :
        dis_hack = 9 
    elif in_hack == 5 :
        dis_hack = 10
    print("\n\n")

def cal_add_cost(c) :
    global add_cost
    if c == 1 :
        add_cost = 70000
    elif c == 2 :
        add_cost = 70000 + 100000
    elif c == 3 :
        add_cost = 70000 + 100000 + 135000
    elif c > 3 :
        add_cost = 70000 + 100000 + 135000
        cc = c - 3 #135000달러 곱하기 횟수
        for i in range(0, cc) :
            add_cost += 135000


def grand_cheet() :
    os.system('cls')
    #print("대 사기극 전용 함수에 진입했습니다.")
    select_team()
    grand_cheet_pass = True
    c = 0
    while grand_cheet_pass : 
        
        os.system('cls')
        print("대 사기극의 보조준비작업은 다음과 같습니다.")
        print("1.순찰 루트")
        print("2.듀건의 화물")
        print("3.보안 정보")
        print("4.파워 드릴")
        print("5.탈출용 위장")
        print("6.보안증")
        print("0.더이상 선택 안함")
        uin1 = 0
        uin1 = only_number(uin1,"[[[구매]]] 항목")
        if uin1 == 0 :
            grand_cheet_pass = False
        elif uin1 == 1 or uin1 == 2 or uin1 == 3 or uin1 == 4 or uin1 == 5 or uin1 == 6 :
            c += 1
    cal_add_cost(c)
        
            


def quietly() :
    os.system('cls')
    #print("비밀 작전 전용 함수에 진입했습니다.")
    select_team()
    quietly_pass = True
    c = 0
    while quietly_pass : 
        print("대 사기극의 보조준비작업은 다음과 같습니다.")
        print("1.순찰 루트")
        print("2.듀건의 화물")
        print("3.보안 정보")
        print("4.파워 드릴")
        print("5.EMP 장치")
        print("6.침투 슈트")
        print("7.보안증")
        print("0.더이상 선택 안함")
        uin1 = 0
        uin1 = only_number(uin1,"[[[구매]]] 항목")
        if uin1 == 0 :
            quietly_pass = False
        elif uin1 == 1 or uin1 == 2 or uin1 == 3 or uin1 == 4 or uin1 == 5 or uin1 == 6 or uin1 == 7:
            c += 1
    cal_add_cost(c)


def just_attack() :
    os.system('cls')
    #print("공격 전술 전용 함수에 진입했습니다.")
    select_team()
    quietly_pass = True
    c = 0
    while quietly_pass : 
        print("대 사기극의 보조준비작업은 다음과 같습니다.")
        print("1.순찰 루트")
        print("2.듀건의 화물")
        print("3.보안 정보")
        print("4.파워 드릴")
        print("5.강화 장갑")
        print("6.굴착기")
        print("7.보안증")
        print("0.더이상 선택 안함")
        uin1 = 0
        uin1 = only_number(uin1,"[[[구매]]] 항목")
        if uin1 == 0 :
            quietly_pass = False
        elif uin1 == 1 or uin1 == 2 or uin1 == 3 or uin1 == 4 or uin1 == 5 or uin1 == 6 or uin1 == 7:
            c += 1
    cal_add_cost(c)

def how_much_your_share() : #how much your share
    print()
    global user_share
    print("이번 습격에서 당신이 받을 몫은 몇퍼센트 인가요?")
    user_share = only_number(user_share,"실제 지분(%)")

    




print("Hello world!")

while p :
    os.system('cls')
    print("카지노 습격 수익 계산기입니다.")
    print("수익계산은 다음과 같은 순서로 이루어집니다.")
    print("1. 목표물 설정")
    print("2. 접근 방식 설정")
    print("3. 총잡이 지정")
    print("4. 운전사 지정")
    print("5. 해커 지정")
    print("6. 접근 방식에 따른 보조준비작업 지정")
    print("\n")
    os.system('pause')
    print()


    os.system('cls')
    print("이번 목표물은 무엇입니까?")
    print("1.현금")
    print("2.금")
    print("3.예술품")
    print("4.다이아몬드")
    print()
    u1_object = 0
    u1_object = only_number(u1_object,"목표물")
    if u1_object == 1 :
        #print("목표물은 현금 입니다")
        n2_object = 1
    elif u1_object == 2 :
        #print("목표물은 금 입니다.")
        n2_object = 2
    elif u1_object == 3 :
        #print("목표물은 예술품 입니다.")
        n2_object = 3
    elif u1_object == 4 :
        #print("몰표물은 다이아몬드 입니다.")
        n2_object = 4
    print("\n\n")



    os.system('cls')
    print("접근 방식은 무엇입니까?")
    print("1. 대 사기극")
    print("2. 비밀 작전")
    print("3. 공격 전술")
    print()
    u2_enter_type = 0
    u2_enter_type = only_number(u2_enter_type, "접근 방식")
    
    check_difficult()
    print("접근 방식은 ",end="")
    if u2_enter_type == 1 :
        print("대 사기극 입니다.")
        grand_cheet()
    elif u2_enter_type == 2 :
        print("비밀 작전 입니다.")
        quietly()
    elif u2_enter_type == 3 :
        print("공격 전술 입니다.")
        just_attack()
    how_much_your_share()
    '''
    n1_object = 0 #하드난이도인지 아닌지 맞으면 1, 아니면 0.
    n2_object = 0 #목표물이 뭔지
    dis_gunner = 0 #총잡이 지분 %
    dis_driver = 0 #운전사 지분 %
    dis_hack = 0 #해커 지분 %
    add_cost = 0 #보조작업 구매로 인해 붙는 추가금액
    user_share = 0 #플레이어의 지분 %
    result = 0 #플레이어의 실제 수익 결과 ($)
    object_cost = 0 #목표 그 자체의 수익금
    '''


    '''
    print("n1_object = ",n1_object)
    print("n2_object = ",n2_object)
    print("dis_gunner = ",dis_gunner)
    print("dis_driver = ",dis_driver)
    print("dis_hack = ",dis_hack)
    print("add_cost = ",add_cost)
    print("user_share = ",user_share)
    print("result = ",result)
    print("object_cost = ",object_cost)
    '''
    object_cost = object_list[n1_object][str(n2_object)]
    


    '''
    print("object_cost =",object_cost)
    print("type(result) =",type(result))
    print("type(object_cost) =",type(object_cost))
    print("type(dis_gunner) =",type(dis_gunner))
    print("type(dis_driver) =",type(dis_driver))
    print("type(dis_hack) =",type(dis_hack))
    '''

    object_cost = int(object_cost)
    result = object_cost
    result = result - ((object_cost // 100) * dis_gunner)
    result = result - ((object_cost // 100) * dis_driver)
    result = result - ((object_cost // 100) * dis_hack)
    result = result - add_cost
    result = (result // 100) * user_share



    print("\n당신의 실제 수익은 {} 달러입니다!\n".format(result))
    os.system('pause')
    

    #습격준비 비용은 생각하지 않는다.
    








