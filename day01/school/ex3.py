print("hello world!")
import csv
a = [[],[],[],[],[],[],[]]
with open('passby_data.csv', 'r') as f :
    reader = csv.DictReader(f)
    print("reader: " , reader)
    #이걸 그냥 출력하면 해당 객체의 위치만 알려주는듯하다
    j = i = 0
    for row in reader :
        a[i].append(row)
        j = j + 1
        if(i%24 == 0) :
            i = i + 1

x_title = ['MON','TUE','MON','THI','FRI','SAT','SUN']
x2_title = []

#a1.append({'num':4,'wnum':0,'ynum':3})
for i in range (0, len(a[i])) :
    day_sum = 0
    for j in range (0, 7) :
        day_sum = int(day_sum) + int(a[j][i])
    print("day_sum = ",day_sum)
    x2_title.append({day_sum})

for i in range (0,len(x2_title[i])) :
    print("x2_title[",i,"] = ",x2_title)


'''


'''





print("finished program")