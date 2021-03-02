tuple_data = 10,20,'tuple',1,123,'string'

arr = []
for i in range(0,len(tuple_data)) :
    arr.append(tuple_data[i])
print(arr)


print("\n\n\n분기점\n\n\n")
'''선생님 답안'''

tuple_data2 = 10,20,'tuple',1,123,'string'
list_data = tuple_data2
print(type(list_data))
print(list_data)

print()
list_data = list(tuple_data2)
print(type(list_data))
print(list_data)



