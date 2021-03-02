'''
리스트 
 - 데이터 다수를 저장하려는 변수

 list_data = [1,2,3]
 list_data = []
'''
list_data1 = [10, 20, 30]
list_data2 = [10, 3.14, 'string']

print('list_data1 : ', list_data1)
print('list_data2 : {}'.format(list_data2))

list_data2 = [40, 50, 60]
list_data1 = list_data1 + list_data2
print('list_data1 : ', list_data1)
print('list_data2 : ', list_data2)

list_data2 *= 3
print('list_data2 : ', list_data2)