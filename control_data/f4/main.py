import csv
import os
import copy as c
table = []
with open('table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        table.append(row)
        #print(row)

a = str(table)
for i in range(len(a)) :
    print(a[i],end='')
    if a[i] == "}" :
        print("")

def setting_product_short_name() :
    global table
    names_product = []
    for i in range(len(table)) :
        if table[i]['1'] not in names_product :
            names_product.append(table[i]['1'])
    #print(names_product)

    names_product2 = []
    for i in range(len(names_product)) :
        names_product2.append(c.deepcopy(names_product[i].split(']')[0]))

    for i in range(len(names_product2)) :
        names_product2[i] = names_product2[i] + ']'

    names_product3 = []
    for i in range(len(names_product2)) :
        if names_product2[i] not in names_product3 :
            #print(names_product2[i])
            names_product3.append(names_product2[i])
    return names_product3
def setting_product_long_name() :
    global table
    names_product = []
    for i in range(len(table)) :
        if table[i]['1'] not in names_product :
            names_product.append(table[i]['1'])
    return names_product





def integrate_subjects() :
    global table
    names_product = setting_product_long_name()
    temp = []
    temp_keys = []
    for i in range(len(names_product)) :
        for j in range(len(table)) :

            if table[j]['1'] == names_product[i] :
                temp.append(table[j])
                





    
count = 0 
for i in range(len(table)) :
    if table[i]['3'] == "특(1등)" :
        count += 1
    
print(count)
print(len(table))