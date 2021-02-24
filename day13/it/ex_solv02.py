'''
3x + 2y = 10 의 해를 구하시오
단 x ,y는 정수이며 , 0<= x,y <= 10을 만족함

'''
c = 0

for x in range(0 , 11) :
    y = 10
    while y > 0 :
        #print("x = {}, y = {}".format(x,y))

        if (3*x + 2*y) == 10 :
            c += 1
            print("x = {}, y = {}".format(x,y))
        y -= 1
    #print()
'''
c = 0

for x in range(0 , 11) :
    for y in range(10,0,-1)
        #print("x = {}, y = {}".format(x,y))

        if (3*x + 2*y) == 10 :
            c += 1
            print("x = {}, y = {}".format(x,y))
        y -= 1
    #print()
'''
'''선생님 풀이'''

for x in range(11) :
    for y in range(11) :
        if (3*x + 2 * y) == 10 :
            print("{}, {}".format(x ,y))















