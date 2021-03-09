def aver_func(*datas) :
    print("type(datas) :",type(datas))
    total = 0
    for i in datas :
        total += i
    return total // len(datas)

res = aver_func(100,80,77)
print("평균 : ",res)