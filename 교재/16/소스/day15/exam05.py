'''
리스트 append(), extend(), insert()
'''
list_data = [10, 20, 30, 40]
list_data.append('a')
list_data.append( [3.14, 'b'] )
print(list_data)
print('len : ', len(list_data))

print('='*10)
list_data = [10, 20, 30, 40]
list_data.extend('a')
list_data.extend( [3.14, 'b'] )
print(list_data)
print('len : ', len(list_data))

print('='*10)
list_data = [10, 20, 30, 40]
list_data.insert(-1, 'a')
list_data.insert(-2, 'c')
print(list_data)
print('len : ', len(list_data))