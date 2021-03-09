def aver_func(list_data) :
    total = 0
    cnt = 0
    for i in list_data :
        total += i
        cnt += 1
    return total / cnt

count = int(input('입력할 데이터의 개수 : '))
list_data = []
for i in range(count) :
    tmp = int(input('{}번째 데이터 입력 : '.format(i+1)))
    list_data.append(tmp)

result = aver_func(list_data)
print('평균 :',result)