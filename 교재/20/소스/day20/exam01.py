def aver_func(*datas) :
    print(type(datas))
    total = 0
    cnt = 0
    for i in datas :
        total += i
        cnt += 1
    if cnt == 0 :
        cnt = 1
        total = 1
    return total / cnt

result = aver_func(100, 80, 77)
print('평균 :',result)

result = aver_func(1,2,3,4,5)
print('평균 :',result)
result = aver_func()
print('평균 :',result)