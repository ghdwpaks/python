'''
리스트에 3개의 정수를 입력받아 합계를 구해 출력하시오.
'''
list_data = [0, 0, 0]
total = 0
for i in range(3) :
    list_data[i] = int(input('{}번째 입력 : '.format(i)))
    total += list_data[i]
print('합계 : ', total)

print('-'*10)
list_data = [0,0,0]
print('list_data : ', list_data)

total = 0
for i in range(3) :
    tmp = int(input('{}번째 입력 : '.format(i)))
    list_data.append(tmp)
    total += list_data[i]
print('합계 : ', total)
print('list_data : ', list_data)