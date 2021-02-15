print("Hello world!")

d1 = int(input("오늘이 몇일인가요?\n>>"))
res = d1 % 7
day = ""
if res == 1:
    day = "월"
elif res ==  2:
    day = "화"
elif res ==  3:
    day = "수"
elif res ==  4:
    day = "목"
elif res ==  5:
    day = "금"
elif res ==  6:
    day = "토"
elif res ==  0:
    day = "일"
print("오늘은 {}요일입니다.".format(day))
    
'''선생님 풀이'''
#날짜를 입력 받아 요일을 구하시오

day = int(input("입력 : "))
result = day % 7
if result == 1 : print("월요일")
if result == 2 : print("화요일")
if result == 3 : print("수요일")
if result == 4 : print("목요일")
if result == 5 : print("금요일")
if result == 6 : print("토요일")
if result == 0 : print("일요일")

if day in (1,8,15,22,29) : print("월요일")
if day in (2,9,16,23,30) : print("화요일")
if day in (3,10,17,24) : print("수요일")
if day in (4,11,18,25) : print("목요일")
if day in (5,12,19,26) : print("금요일")
if day in (6,13,20,27) : print("토요일")
if day in (7,14,21,28) : print("일요일")













