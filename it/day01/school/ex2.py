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

#a1.append({'num':4,'wnum':0,'ynum':3})
x_title = ['MON','TUE','MON','THI','FRI','SAT','SUN']
for i in range (0, 7) :
    for j in range (0, len(a[i])) :
        print(x_title[i], "[", j, "] = ",a[i][j])



print("finished program")