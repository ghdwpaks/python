def a(e) :
    t = 0
    for i in range(1,e + 1) :
        t += i
    return t
e = int(input("입력 : "))

t = a(e)
print("1~{}까지의 합계 : {}".format(e,t))

t = a(20)
print("1~{}까지의 합계 : {}".format(e,t))