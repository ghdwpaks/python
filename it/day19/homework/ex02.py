'''
절댓값을 반환하는 함수를 만들어주세요
'''
def f2(a) :
    if a >= 0 :
        return a
    elif a < 0 :
        return -a

print("{}의 절댓값은 {}입니다!".format(-10,f2(-10)))
print("{}의 절댓값은 {}입니다!".format(10,f2(-10)))
