tuple_data = 10,20,30,40,50

print('tuple_data[1:3] : ', tuple_data[1:3])
print('tuple_data[1:] : ', tuple_data[1:])
print('tuple_data[:3] : ', tuple_data[:3])

total = 0
for i in tuple_data :
    total += i
print('합계 : ', total)

tuple_data2 = 100, 200, 'string'
data1, data2, data3 = tuple_data2

print('{}, {}, {}'.format(data1, data2, data3))

data, *list_data = tuple_data2
print('{}, {}'.format(data, list_data))
