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
for i in range(len(t)) :
    
    if t[i]['3'] == '-' :
        pass
    else : 
        temp.append(float(t[i]['3']))
print(temp)
temp.sort(reverse=True)
#print("\n\n\n\n")
print(temp[0])
