import copy

dict_data1 = {'id' : 'kyes'}
dict_data2 = dict_data1 # 얕은 복사
dict_data2 = copy.deepcopy(dict_data1) # 깊은 복사

print(dict_data1)
print(dict_data2)

print('-'*8)

dict_data1.clear()
print(dict_data1)
print(dict_data2)