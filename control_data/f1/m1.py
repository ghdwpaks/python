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
        
        if t[i][str(target)] == '-' :
            count_trash += 1
        else : 
            temp.append(float(t[i][str(target)]))
    temp.sort(reverse=True)
    lent = int(len(t) - count_trash)
    if target == 2 :
        subject1 = "15세이상인구";subject2 = "천명"
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
        
        if t[i][str(target)] == '-' :
            pass
        else : 
            print(t[i][str(target)]+"+",end="")
            sum += float(t[i][target])
    print("{:.2f}".format(sum))
def show_rank() :
    global target,temp,lent,count_trash
    Rotating_target = 0
    print("2target =",Rotating_target)
    print("type target =",type(Rotating_target))
    
    pas = True
    while pas :
        for i in range(len(t)) :
            #print(t[i][str(target)])
            if t[i][str(target)] == '-' :
                pass
            else : 
                
                if float(t[i][str(target)]) == temp[Rotating_target] :
                    print("{}(이)가 {}번째로 높은 도시는 \t{} 로 \t{} {}입니다.".format(subject1,Rotating_target+1,t[i]['1'],t[i][str(target)],subject2))
                    Rotating_target += 1 
                    if Rotating_target >= lent :
                        pas = False
                        break
#print(t)
target = 9
set_rank()
#print(temp)
show_rank()


