'''
0~100점의 점수를 입력하면 A~F까지의 학점을 반환하는 함수를 만들어주세요.
'''
def f3(g) :
    if g > 89 :
        return 'A'
    elif g > 79 :
        return "B"
    elif g > 69 :
        return "C"
    elif g > 59 :
        return "D"
    elif g > 49 :
        return "E"
    elif g <= 49 :
        return "F"
def f4(g) :
    if g > 100 or g < 0 :
        return 0
    else :
        return f3(g)
for i in range(-10,110) :
    if f4(i) == 0 :
        print("입력이 잘못되었습니다.")
    else :
        print(f4(i))
