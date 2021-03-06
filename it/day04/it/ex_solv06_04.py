'''
1.올해 년도와 태어난 년도 4자리를 입력 받아 나이를 계산하는 프로그램을 작성하시오
'''
this_year = int(input("올해 년도를 입력해주세요.>>"))
born_year = int(input("태어난 년도를 입력해주세요.>>"))

age = this_year - born_year
print("당신의 나이는 {}살 입니다.".format(age+1))

'''선생님 풀이'''

current_year = int(input('현재년도 : '))
birth_year = int(input('탄생년도 : '))
age = current_year - birth_year + 1
print('나이는 {}살입니다.'.format(age))

first_weight = float(input('첫 번째 물건의 무게를 입력하시오?'))
second_weight = float(input('두 번째 물건의 무게를 입력하시오?'))
weight = 600 - (first_weight + second_weight)
print('현재 엘리베이터에 허용무게는 {:.2f}kg 입니다.'.format(weight))