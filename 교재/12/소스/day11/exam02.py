
# 1 ~ x 입력 받은 수 까지의 합계를 구해보자.

end = int(input('입력 : '))
i = 1; total = 0
while i <= end :
    total += i
    i += 1
print('1 ~ {}의 합계 : {}'.format(end ,total))