def sum_func(end=100, begin=1):
    total = 0
    for i in range(begin, end+1) :
        total += i
    return total

total = sum_func()
print('합계 : {}'.format(total))

total = sum_func(10)
print('합계 : {}'.format(total))

total = sum_func(20, 11)
print('합계 : {}'.format(total))
