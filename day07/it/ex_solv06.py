print("Hello world!")
'''
국,영,수 점수를 입력 받아 평균 60점 이상, 과목 점수가 40점 이상이면 합격이다.
그 외는 불합격, 불합격일 경우에는 사유를 출력한다 ."평균 불합격", "수학 과목 불합격"
'''


nm = input("이름 : ")
k = int(input("국어 점수 : "))
e = int(input("영어 점수 : "))
m = int(input("수학 점수 : "))
res_k = True
res_e = True
res_m = True
res = True

avg = (k + e + m) / 3
if k < 40 :
    res_k = False
if e < 40 : 
    res_e = False
if m < 40 :
    res_m = False

if avg < 60 :
    print("평균 불합격 ")
    res = False
if not res_k :
    print("국어 과목 불합격 ")
    res = False
if not res_e :
    print("영어 과목 불합격 ")
    res = False
if not res_m :
    print("수학 과목 불합격 ")
    res = False

if res :
    print("합격하셨습니다!")





