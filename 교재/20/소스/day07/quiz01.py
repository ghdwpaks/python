# 이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 
# 평균이 90이상이면 ‘A’, 80 이상‘B’, 70이상 ’C’, 60이상 ‘D’, 
# 60미만이면 ‘F’ 를 출력 하시오.
# name = input('이름 : ')
# number = input('학번 : ')
# kor = int(input('국어 점수 입력 : '))
# eng = int(input('영어 점수 입력 : '))
# math = int(input('수학 점수 입력 : '))

# sum_data = kor + eng + math
# avg = sum_data / 3
# grade = ''
# if avg >= 90 :
#     grade = 'A'
# elif avg >= 80 :
#     grade = 'B'
# elif avg >= 70 :
#     grade = 'C'
# elif avg >= 60 :
#     grade = 'D'
# else :
#     grade = 'F'

# print('이름 : {}'.format(name))
# print('학번 : {}'.format(number))
# print('합계 : {}, 평균 : {:.2f}'.format(sum_data, avg))
# print('학점 : {}학점'.format(grade))

# 커피의 개당 가격은 2000원이다. 
# 10개 초과하면 초과하는 양에 대해서만 
# 개당 1500원씩 받는다. 
# 커피의 개수를 입력 받아 금액을 출력하시오.
coffee = int(input('커피 개수 입력 : '))
cost = 0
if coffee > 10 :
    cost = 20000 + (coffee - 10) * 1500
elif coffee <= 0 :
    cost = 0
else :
    cost = coffee * 2000
print('{}잔은 {}원입니다.'.format(coffee, cost))