table = []

import csv
with open('table2.csv','r') as f :
        reader = csv.DictReader(f)
        for row in reader :
            table.append(row)

print(table)
print(csv.DictReader)


a = str(table)
for i in range(len(a)) :
    print(a[i],end='')
    if a[i] == "}" :
        print("")