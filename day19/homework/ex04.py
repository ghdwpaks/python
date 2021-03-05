'''
수를 입력하여 소수이다/아니다를 판별하는 함수를 만들어주세요

'''
def f5(n) :
    for i in range(2,n) :
        if n % i == 0 :
            return False
    return True

u = int(input("입력 : "))

if f5(u) :
    print("{}는 소수입니다.".format(u))
else :
    print("{}는 소수가 아닙니다.".format(u))
            
    






