'''

1~100사이에 있는 자연수에 대하여 자기 자신의 수를 제외한 모든 약수의 합이 자신과 같아지는 수(완전수)를 구하여라
예 6의 약수 = 1,2,3,6
1+2+3 = 6(완전수)
'''
print("1~101까지의 완전수는 ",end="")
for i in range(1, 101) :
    mea = [] #약수 리스트
    for j in range(1,i) :
        if i % j == 0 :
            mea.append(j)
    res = sum(mea)
    if res == i :
        print(i,end="")
print("가 있습니다!")

'''선생님 답안'''

print()
print("완전수 : ",end="")
total = 0
for i in range(1,30) :
    for j in range(1,i) :
        if i % j == 0 :
            total += j
    if i == total :
        print("{}, ".format(i),end="")
    total = 0





