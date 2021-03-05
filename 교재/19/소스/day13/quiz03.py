# 3x + 2y = 10의 해를 구하세요. 
# 단 x, y는 정수이며, 0<= x, y <= 10을 만족함.

for x in range(11) :
    for y in range(11):
        if (3*x + 2*y) == 10 :
            print('{}, {}'.format(x, y))

# 세 자리의 수 중 1, 2, 3 으로 구성된 수들을
# 오름차순 나열 했을 때, 14 번째 위치한 수를 출력 하시오.
# 예) 111, 112, 113...
print()
count = 0
for i in range(1,4) :
    for j in range(1,4) :
        for k in range(1,4) :
            count += 1
            if count == 14 :
                print('{}'.format(i*100+j*10+k))