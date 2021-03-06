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

x_title = ['MON','TUE','WED','THI','FRI','SAT','SUN']
x2_title = []

for i in range (0, 7) :
    for j in range (0, len(a[i])) :
        print(x_title[i], "[", j, "] = ",a[i][j])

print("\n\n분기점\n\n")
print("a[0][0]['num'] = " , a[0][0]['num'])

#a1.append({'num':4,'wnum':0,'ynum':3})
for i in range (0, len(a[i])) :
    day_sum = 0
    for j in range (0, 7) :
        print("a[j][i]['num'] = " , a[j][i]['num'])
        day_sum = day_sum + a[i][j]['num']
    print("day_sum = ",day_sum)
    x2_title.append({day_sum})

for i in range (0,len(x2_title)) :
    print("x2_title[",i,"] = ",x2_title)


'''


'''





print("finished program")