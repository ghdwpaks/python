import copy

list_data1 = [1, 2, 3]
list_data2 = list_data1 # 얕은 복사
list_data2 = copy.deepcopy(list_data1) # 깊은 복사

print(list_data1)
print(list_data2)

print('-'*8)

list_data1.clear()
print(list_data1)
print(list_data2)

print('-'*8)
list_data1 = copy.deepcopy(list_data2) # 깊은 복사
print(list_data1)
print(list_data2)

print('-'*8)
list_data2.append(4)
print(list_data1)
print(list_data2)