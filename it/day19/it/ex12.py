'''
start, end 인자를 사용하는 rangedRand(start,end) 함수를 만들고
start ~ end 까지 랜덥 값을 반환 하도록 하시오
'''
def ps(e,s) :
    r = random.randrange(s,e)
    return r 
import random
print("Hello world!")

s = int(input("시작점 : "))
e = int(input("끝점 : "))
r = ps(e,s)
print("{}과{}사이의 랜덤수는 {}입니다.".format(s,e,r))

def rangeRand(s,e) :
    return s + int(random() * (end - start +1))
for i in random(10) :
    rangeRand(1,10)