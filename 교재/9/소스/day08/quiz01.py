# 학점을 입력 받아 구문하여 문자열 출력.
# 입력 데이터는 문자 A - F
# A와B는 “참 잘했어요“
# C와D는 “분발합시다.“
# F는 아무것도 출력하지 않는다.
grade = input('학점 입력 : ')
print_string = ''

if grade == 'A' or grade == 'B':
    print_string ='참 잘 했어요.'
elif  grade == 'C' or grade == 'D':
    print_string ='분발 합시다.'

print('{}학점은 {}'.format(grade, print_string))


# 국,영,수 점수를 입력 받아 평균 60점 이상,  과목 점수가 40점 이상이면 합격이다.
# 그 외는 불합격, 불합격 일 경우는 사유를 출력한다. “평균 불합격, “어떤 과목 불합격”
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
math = int(input('수학 점수 입력 : '))
avg = (kor + eng + math) / 3
if avg >= 60 :
    if kor < 40 :
        print_string = '국어 과목 {}점으로 불합격'.format(kor)
    elif eng < 40 : 
        print_string = '영어 과목 {}점으로 불합격'.format(eng)
    elif math < 40 :
        print_string = '수학 과목 {}점으로 불합격'.format(math)
    else :
        print_string = '합격'
else :
    print_string = '평균 {:.2f}점으로 불합격'.format(avg)

print(print_string)