

'''
출력 결과
name : shoes
date : 03/02
price : 59000

name : coffee
date : 03/03
price : 2500

name : food
date : 03/04
price : 7000

name : dress
date : 03/13
price : 130000
'''
accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
tmp = accountBook.split(',')
list_data = []
for i in tmp :
    i = i.lstrip();
    list_data.append(i.split(' '))

for data in list_data :
    print('name : ', data[0])
    print('date : ', data[1])
    print('price : ', data[2])
    print()