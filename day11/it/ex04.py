print("Hello world!")

summ = 0
i = 0
while i < 11 :
    if i % 2 == 1 :
        summ += i
    i += 1
print("1 ~ 10의 홀수 합계 : {}".format(summ))

summ = 0
i = 0
end = int(input("입력 : "))
while i < end+1 :
    if i % 2 == 1 :
        summ += i
    i += 1
print("1 ~ {}의 홀수 합계 : {}".format(end,summ))
