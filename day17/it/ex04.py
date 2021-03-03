import copy
list_data1 = {'id' : 'kyes'}
list_data2 = list_data1 #얕은복사
list_data2 = copy.deepcopy(list_data1)#깊은 복사

print(list_data1)
print(list_data2)

print("=========")
list_data1.clear()

print(list_data1)
print(list_data2)


