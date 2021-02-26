
# 2에서부터 입력된 어떤 수까지 내에 있는 
# 소수를 찾는 프로그램을 작성하라.
# 입력 : 100
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 
# 61 67 71 73 79 83 89 97

data = int(input('입력 : '))
count = 0
for i in range(2, data+1) : 
    for j in range(2, i+1) : 
        if i % j == 0 :
            count += 1
    if count == 1 :
        print('{} '.format(i), end='')
    count = 0

# 1~1000사이에 있는 자연수에 대하여 자기 자신의 수를
# 제외한 모든 약수의 합이 자신과 같아지는 수(완전수)를 구하여라.
# 예) 6의 약수= 1, 2, 3, 6
# 1+2+3=6(완전수)
# 1~1000에서 완전수의 개수는 3개
print()
print('완전수 : ', end='')
total = 0
for i in  range(1, 30) :
    for j in range(1, i) :
        if i % j == 0 :
            total += j
            #print('{} + '.format(j), end='')
    #print()
    if i == total :
        print('{}, '.format(i), end='')

    total = 0