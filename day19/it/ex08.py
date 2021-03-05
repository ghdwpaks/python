def a(s,e) :
    t = 0
    for i in range(s,e + 1) :
        t += i
    return t
s = int(input("시작 :"))
e = int(input("끝 : "))
t = a(s,e)
print("1~{}까지의 합계 : {}".format(e,t))

t = a(1,20)
print("1~{}까지의 합계 : {}".format(e,t))