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
#경제 활동 인구 economically active population
#def eap_t () :
sum = 0.0
for i in range(len(t)) :
    
    if t[i]['3'] == '-' :
        pass
    else : 
        print(t[i]['3']+"+",end="")
        sum += float(t[i]['3'])
print("{:.2f}".format(sum))
print("\n\n\n\n")
temp = []
count_trash = 0
for i in range(len(t)) :
    
    if t[i]['3'] == '-' :
        count_trash += 1
    else : 
        temp.append(float(t[i]['3']))
#print(temp)
temp.sort(reverse=True)
#print("\n\n\n\n")
'''
print(temp[0])
for i in range(len(temp)) :
    print("{}   {}".format(temp[5],t[i]['3']))
'''
target = 0
pas = True
while pas :
    for i in range(len(t)) :
        if t[i]['3'] == '-' :
            pass
        else : 
            
            #print(temp[5] , "" ,t[i]['3'])
            if float(t[i]['3']) == temp[target] :
                print("경제횔동인구가 {}번째로 높은 도시는 \t{} 로 \t{} 천명입니다.".format(target+1,t[i]['1'],t[i]['3']))
                '''
                print(target + 1)
                print(len(t) - count_trash)
                '''
                target += 1 
                if target >= (len(t) - count_trash) :
                    pas = False
                    break
                #print(True)
            else :
                #print(False)
                pass