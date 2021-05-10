import csv
import os
import copy as c
table = []
with open('table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        table.append(row)
        #print(row)
'''
a = str(table)
for i in range(len(a)) :
    print(a[i],end='')
    if a[i] == "}" :
        print("")
'''
