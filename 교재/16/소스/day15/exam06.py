'''
리스트 index(), count()
'''

list_data = [11, 22, 33]
data = int(input('입력 : '))
print('데이터 {}의 index는 {}이다. '.format(data, list_data.index(data)))

list_data.append(11)
print(list_data)
data = int(input('입력 : '))
print('데이터 {}의 count {}개이다. '.format(data, list_data.count(data)))
