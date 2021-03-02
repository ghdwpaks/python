# 369 

data = int(input('입력 : '))
count = 0
for i in range(1, data+1) :
    j = i
    while True :
        if j == 0 : break
        tmp = j % 10
        j //= 10
        if tmp == 3 or tmp == 6 or tmp == 9 :
            print(i)
            count += 1
print('출력 :', count)