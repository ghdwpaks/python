accouBook= 'shoes 03/02 59000, coffee 03/03 2500, food 03/03 7000, dress 03/13 130000'

tmp = accouBook.split(',')
list_data = []
for i in tmp :
    i = i.lstrip()
    list_data.append(i.split(" "))

for data in list_data :
    print("name : ",data[0])
    print("data : ",data[1])
    print("price : ",data[2])
    print()