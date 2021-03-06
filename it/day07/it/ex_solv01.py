'''
이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 평균이 90이상이면 'A', 80이상 'B' , 70이상 'C', 60이상 'D', 60 미만이면 'F'를 출력하시오
'''
name = input("이름 : ")
num = input("학번 : ")

score_math = int(input("수학점수 입력 : "))
score_korean = int(input("국어점수 입력 : "))
score_python = int(input("파이썬점수 입력 : "))

sum_all = score_korean + score_math + score_python
avg = sum_all / 3

print("{}({})님의 등급은".format(name,num),end="")
if avg >= 90 :
    print("A",end="")
elif avg >= 80 :
    print("B",end="")
elif avg >= 70 :
    print("C",end="")
elif avg >= 60 :
    print("D",end="")
elif avg < 60 :
    print("F",end="")
print("이며\n평균점수는 {}점 입니다!".format(avg))

print("\n\n\n분기점\n\n\n")

'''선생님 풀이'''
name = input("이름 : ")
number = input("학번 : ")
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))

sum_data = kor + eng + math
avg = sum_data / 3

if avg >= 90 :
    grade = 'A'
elif avg >= 80 :
    grade = 'B'
elif avg >= 70 :
    grade = 'C'
elif avg >= 60 :
    grade = 'D'
else :
    grade = "F"
print("이름 : {}".format(name))
print("학번 : {}".format(number))
print("합계 : {}, 평균 : {:.2f}".format(sum_all,avg))
print("학점 : {}학점".format(grade))












