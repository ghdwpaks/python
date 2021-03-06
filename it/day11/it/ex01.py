'''
1에서 1000 사이 자연수 중에 수를 구성하는 개개의 수가 서로 연속적으로 되어 있는 수를 찾아 출력하는 프로그램을 작성하세요.
'''

print("Hello world!")
for i in range(1 , 10 ) :
    for j in range(1 , 100) :
        if j // i == 11 and j % i == 0 :
            print(j,end="")
            print(" , ",end="") 

for i in range(1 , 10 ) :
    for j in range(1 , 1000) :
        if j // i == 111 and j % i == 0 :
            print(j,end="")
            print(" , ",end="") 
print("\n\n분기점\n\n")
    
'''선생님 답안'''
for i in range(1, 1001) :
    data1 = i % 10
    data2 = i // 10 % 10
    data3 = i // 100
    if data1 == data2 and data3 == 0 :
        print("{} ".format(i),end="")
    if data1 == data2 and data1 == data3 :
        print("{} ".format(i),end="")