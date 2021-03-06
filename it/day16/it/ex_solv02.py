import random
numbers = [10,20,30,40,50,60,70]

total = 0

for i in numbers :
    total += i
print("{}의 합계 : {}".format(numbers,total))


numbers = []
count = 0
while True :
    tmp = random.randrange(1,46)

    if tmp not in numbers :
        numbers.append(tmp)

    count += 1
    if count == 6 :
        break
print("중복 없는 6개의 랜덤 데이터 :",numbers)



