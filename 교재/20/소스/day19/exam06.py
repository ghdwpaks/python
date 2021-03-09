
end = int(input('입력 : '))
total = 0
for i in range(1, end+1) :
    total += i
print('1~{}까지의 합계 : {}'.format(end, total))