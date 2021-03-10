
print("Hello world!")
def get_cal_type() :
    while True:
        print("1. 더하기(+)\n2. 빼기(-)")
        u = input("계산방식 : ")
        if u == "+" or u == "1" :
            return True
        elif u == "-" or u == "2" :
            return False
        
def get_under(s) :
    res = 0
    if s[0] == 1 :
        res += 0.5
    elif s[1] == 1:
        res += 0.25
    elif s[2] == 1 :
        res += 0.125
    return res


while True :
    print("이 계산기는 소수점 3자리까지만 계산할 수 있습니다.")
    u1 = input("첫번째 수 입력 : ")
    u1 = u1.split(".")
    u2 = input("두번째 수 입력 : ")
    u2 = u1.split(".")
    
    u3 = get_cal_type()
    r1 = r2 = res = 0
    if u3 :
        r1 = bin(u1[0]) + bin(u2[0])
        tr1 = get_under(u1[1])
        tr2 = get_under(u2[1])
        r2 = tr1 + tr2
        res = r1+r2
    else :
        r1 = bin(u1[0]) - bin(u2[0])
        tr1 = get_under(u1[1])
        tr2 = get_under(u2[1])
        r2 = tr1 - tr2
        res = r1+r2
    print("결과 :",res)




