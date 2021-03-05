'''
리스트 
 - 인덱싱
 list_data = [10,20,30,40]
 시작은 0부터 순차적으로 데이터 한 개씩 접근이 가능하다.

'''
list_data = [10,20,30,40]
for i in list_data : 
    print('{} '.format(i))

print('list_data 길이 : ', len(list_data))

for i in range(len(list_data)) :
    list_data[i] = list_data[i] * 10

for i in range(len(list_data)) :
    print('{} '.format(list_data[i]))

print(list_data)
