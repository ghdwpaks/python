def sum_func(begin, end):
    total = 0
    for i in range(begin, end+1) :
        total += i
    return total
   
begin = int(input('시작 : '))
end = int(input('끝 : '))

total = sum_func(begin, end)
print('{}~{}까지의 합계 : {}'.format(begin, end, total))
