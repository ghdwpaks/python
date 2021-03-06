'''
윤년을 구하는 코드를 작성하시오
	4의 배수는 윤년이 된다. 그 외는 평년
	4의 배수이면서 100의 배수인 경우는 평년이다 .그 외는 윤년
	4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그 외는 평년
'''
y = int(input("올해 년도 : "))

print_y = "평년"
if y % 4 == 0 :
    print_y = "윤년"
    if y % 100 == 0 :
        print_y = "평년"
        if y % 400 == 0 :
            print_y = "윤년"

print("올해는 {}입니다.".format(print_y))

print("\n\n\n분기점\n\n\n")

'''선생님 풀이'''

year = int(input("연도 입력 : "))
result = ""
if year % 4 == 0 :
    result = "윤년"
    if year % 100 == 0 :
        result = "평년"
        if year % 400 == 0 :
            result = "윤년"

print("{}년은 {}입니다.".format(year,result))