'''
비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 10분 단위로 추가 요금 5000원씩 부가된다. 비행기 탈 시간을 입력하여 요금 계산기를 만드시오
'''
print("Hello world!")

t = int(input("몇분거리 : "))
tt = 0
b = 0
c = 0
if t <= 0 :
    print("요금이 부과되지 않습니다.")
else :
    c = 30000
    if t <= 30 :
        tt = 0
    else :
        tt = t - 30
        if tt < 10 :
            b = 5000
        else :
            while tt > 10 :
                tt -= 10
                b += 5000
            b += 5000
    
    print("기본요금 {}원에 추가요금 {}원이 붙어서 총\n{}원입니다.".format(c,b,c+b))

print("\n\n\n분기점\n\n\n")

'''선생님 풀이'''
time = int(input("비행기 이용시간(분) : "))
time -= 30

if time <= 0:
    cost = 30000
elif time % 10 == 0 :
    cost = 30000 + (time // 10) * 5000 #이용시간이 10분, 30분 등등 10분단위로 나뉘어 떨어지는 경우
else :
    cost = 30000 + (time // 10 + 1) * 5000#이용시간이 44분, 53분 등등 10분단위로 나뉘어 떨어지지 않는 경우

print("비행기 이용시간은 {}분으로 요근은 {:,}원 입니다.")

'''선생님 풀이 두번째'''
time = int(input("비행기 이용시간(분) : "))
time -= 30

if time <= 0:
    cost = 30000
elif time % 10 == 0 :
    cost = 30000 + (time // 10) * 5000 #이용시간이 10분, 30분 등등 10분단위로 나뉘어 떨어지는 경우
else :
    cost = 30000 + (time // 10 + 1) * 5000#이용시간이 44분, 53분 등등 10분단위로 나뉘어 떨어지지 않는 경우






