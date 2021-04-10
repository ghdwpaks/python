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
def set_rank() :
    global target,lent,count_trash
    print("target =",target)
    print("type target =",type(target))
    for i in range(len(t)) :
        
        if t[i]['3'] == '-' :
            count_trash += 1
        else : 
            temp.append(float(t[i]['3']))
    temp.sort(reverse=True)
    lent = int(len(t) - count_trash)
def get_total() :
    sum = 0.0
    global target
    target = str(target)
    for i in range(len(t)) :
        
        if t[i][target] == '-' :
            pass
        else : 
            print(t[i][target]+"+",end="")
            sum += float(t[i][target])
    print("{:.2f}".format(sum))
def show_rank() :
    global target
    pas = True
    while pas :
        for i in range(len(t)) :
            if t[i]['3'] == '-' :
                pass
            else : 
                if float(t[i]['3']) == temp[target] :
                    print("경제횔동인구가 {}번째로 높은 도시는 \t{} 로 \t{} 천명입니다.".format(target+1,t[i]['1'],t[i]['3']))
                    target += 1 
                    if target >= lent :
                        pas = False
                        break
target = 1
set_rank()
print(temp)


