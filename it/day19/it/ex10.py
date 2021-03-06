def a(d=30,t=8,w=8500) :
    r = d * t * w
    return r

n = int(input("1. 기본급\n2. 일별 계산\n3. 시간까지 계산\n4. 시급까지 계산\n선택 : "))

if n == 1 :
    r = a()
elif n == 2:
    d = int(input("일한 날짜 입력(몇일) : "))
    r = a(d)
elif n == 2:
    d = int(input("일한 날짜 입력(몇일) : "))
    t = int(input("하루 근무 시간(몇시간) : "))
    r = a(d,t)
elif n == 4:
    d = int(input("일한 날짜 입력(몇일) : "))
    t = int(input("하루 근무 시간(몇시간) : "))
    w = int(input("시급(원) : "))
    r = a(d,t,w)



print("급여 : {:,}원 입니다.".format(r))