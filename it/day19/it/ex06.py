def a(e) :
    t = 0
    for i in range(1,e + 1) :
        t += i
    print("1~{}까지의 합계 : {}".format(e,t))
a(10)