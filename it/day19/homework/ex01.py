'''
두 수를 입력받아 큰 수를 반환하는 함수를 만들어주세요.

'''
def f1(a,b ) :
    if a > b :
        print("{}보다 {}가 더 큽니다.".format(b,a))
    elif a < b :
        print("{}보다 {}가 더 큽니다.".format(a,b))
    else :
        print("{}와 {}는 같은 수입니다.".format(a,b))

f1(10,5)
f1(5,10)
f1(10,10)



