def sum_func(end):
    total = 0
    for i in range(1, end+1) :
        total += i
    return total
   
end = int(input('입력 : '))
total = sum_func(end)
print('1~{}까지의 합계 : {}'.format(end, total))

total = sum_func(20)
print('1~{}까지의 합계 : {}'.format(20, total))