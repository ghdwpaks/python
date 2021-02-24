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
    




