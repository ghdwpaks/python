'''
2부터 입력된 어떤 수까지 내에 있는 소수를 찾는 프로그램을 작성하라.
'''
lim = int(input("정수 입력")) + 1
lis = []
for i in range(2,lim) :
    res = 1
    for j in range(2 , i) :
        if i % j == 0 :
            res = 0
            break
    if res == 1 : 
        lis.append(i)

print("lis :",lis)
    

'''선생님 답안'''

data = int(input("입력 : "))
count = 0
for i in range(2 , data+1) :
    for j in range(2 , i+1) :
        if i % j == 0 :
            count += 1
        if count == 1 :
            print("{} ".format(i))
        count = 0
