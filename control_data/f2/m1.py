print("Hello world!")
import csv
import os
t = []
with open('table1.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        t.append(row)
        print(row)
print("Hello world!")
print(t)
target = 0 #도시 타겟 지정
city = "" #도시이름
sex = '' #성별