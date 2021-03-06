list_data1 = [1,2,3]
'''
[1,2,3]이라는 데이터를 '가리키는'객체인 
'''
list_data2 = list_data1
list_data3 = list_data2

print(list_data1)
print(list_data2)
print(list_data3)
print("=========")
list_data1.clear()
print(list_data1)
print(list_data2)
print(list_data3)




