def a(e,s=1) :
    t = 0
    print("s :",s)
    print("e :",e)
    for i in range(s,e + 1) :
        t += i
    return t

s = int(input("시작 :"))
e = int(input("끝 : "))
print("s :",s)
print("e :",e)
t = a(e,s )

print(1)
print("t :",t)
print("{}~{}까지의 합계 : {}".format(s,e,t))

print(2)
t = a(20)
print("t :",t)
print("1~{}까지의 합계 : {}".format(20,t))