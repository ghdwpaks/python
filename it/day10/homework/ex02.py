from random import *

print("Hello world!")
print("업다운 게임을 시작합니다!")
print("스무고개를 하며 목표 숫자를 맞추면 됩니다.")
print("범위는 1 부터 100까지입니다!")
ran = randint(1, 100)
p = False
#print("ran =",ran)
for i in range(0 ,20) :
    print("현재 도전 가능 기회 :",20-i)
    u = int(input("숫자 입력 : "))
    if u == ran :
        print("맞추셨습니다!")
        p = True
        break
    elif u > ran :
        print("목표 수치는 지금보다 더 아래에 있습니다!")
    elif u < ran :
        print("목표 수치는 지금보다 더 위에 있습니다!")
    print("\n\n")
    

if not p :
    print("정답은 {}였습니다!".format(ran))





