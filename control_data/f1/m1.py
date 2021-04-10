print("Hello world!")
import csv
import os
t = []
with open('table_type1.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        t.append(row)
        #print(row)
print("Hello world!")
count_trash = 0
temp = []
lent = 0
target = 0
subject1 = ""
subject2 = ""
def set_rank() :
    global subject1,subject2 ,target,lent,count_trash
    print("1target =",target)
    print("type target =",type(target))
    for i in range(len(t)) :
        
        if t[i][str(target)] == '-'or t[i][str(target)] == '*' :
            count_trash += 1
        else : 
            temp.append(float(t[i][str(target)]))
    temp.sort(reverse=True)
    lent = int(len(t) - count_trash)
    if target == 2 :
        subject1 = "15세이상인구 ";subject2 = "천명"
    elif target == 3:
        subject1 = "경제활동인구";subject2 = "천명"
    elif target == 4:
        subject1 = "취업자";subject2 = "천명"
    elif target == 5:
        subject1 = "실업자";subject2 = "천명"
    elif target == 6:
        subject1 = "실업자";subject2 = "C.V."
    elif target == 7:
        subject1 = "비경제활동인구";subject2 = "천명"
    elif target == 8:
        subject1 = "경제활동참가율";subject2 = "％"
    elif target == 9:
        subject1 = "고용률";subject2 = "％"
    elif target == 10:
        subject1 = "15~64세 고용률";subject2 = "％"
    elif target == 11:
        subject1 = "실업률";subject2 = "％"
    elif target == 12:
        subject1 = "실업률";subject2 = "C.V."

def get_total() :
    sum = 0.0
    global target
    for i in range(len(t)) :
        
        if t[i][str(target)] == '-' or t[i][str(target)] == '*' :
            pass
        else : 
            #print(t[i][str(target)]+"+",end="")
            sum += float(t[i][str(target)])
    print("{:.2f}".format(sum))
    print("{}의 총합은{:.1f}{}입니다.".format(subject1,sum,subject2))
    os.system("pause")
    return sum
def show_rank() :
    global target,temp,lent,count_trash
    Rotating_target = 0
    print("2target =",Rotating_target)
    print("type target =",type(Rotating_target))
    
    pas = True
    while pas :
        for i in range(len(t)) :
            #print(t[i][str(target)])
            if t[i][str(target)] == '-' or t[i][str(target)] == '*' :
                pass
            else : 
                
                if float(t[i][str(target)]) == temp[Rotating_target] :
                    print("{}(이)가 {}번째로 높은 도시는 \t{} 로 \t{} {}입니다.".format(subject1,Rotating_target+1,t[i]['1'],t[i][str(target)],subject2))
                    Rotating_target += 1 
                    if Rotating_target >= lent :
                        pas = False
                        break
    os.system("pause")

def choose_func(subject_main) :
    global target
    p2 = True
    target = subject_main
    set_rank()
    while p2 :
        os.system("cls")
        print("0.뒤로가기")
        print("1.순위별로 출력")
        if subject_main == 7 or subject_main == 8 or subject_main == 9 or subject_main == 10 or subject_main == 11 :
            pass
        else :
            print("2.총합 출력")
        u2 = input("종류선택 : ")
        if "exit" == u2 or "종료" == u2 or '0' == u2 or "EXIT" in u2:
            p2 = False
        elif u2 == '' :
            continue
        elif int(u2) == 1 :
            show_rank()
        elif int(u2) == 2 :
            get_total()
        else :
            continue
'''
#print(t)
target = 5
set_rank()
#print(temp)
#show_rank()
res1 = get_total()
'''
print("Hello world!")
print("")
p = True
while p :
    os.system("cls")
    print("1.15세이상인구")
    print("2.경제활동인구")
    print("3.취업자")
    print("4.실업자")
    print("5.실업자(C.V.)")
    print("6.비경제활동인구")
    print("7.경제활동참가율(%)")
    print("8.고용률(%)")
    print("9.15~64세 고용률(%)")
    print("10.실업률(%)")
    print("11.실업률(C.V.)")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    elif int(u) < 12 and int(u) > 0 :
        choose_func(int(u)+1)
    else :
        continue
