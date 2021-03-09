#올해 년도와 태어난 년도 4자리를 입력 받아 나이를 
#계산하는 프로그램을 작성하시오.
current_year = int(input('현재년도 : '))
birth_year = int(input('탄생년도 : '))
age = current_year - birth_year + 1
print('나이는 {}살 입니다.'.format(age))

# 600kg 제한의 화물용 엘리베이터가 있다. 
# 2개의 물건에 대한 무게를 실수로 입력 받아 
# 현재 엘리베이터에 더 적재할 수 있는 무게를 구하시오.
# 첫 번째 물건의 무게를 입력하시오? 64.27
# 두 번째 물건의 무게를 입력하시오? 75.25
# 현재 엘리베이터에 허용무게는 460.48kg 입니다.

first_weight = float(input('첫 번째 물건의 무게를 입력하시오? '))
second_weight = float(input('두 번째 물건의 무게를 입력하시오? '))
weight = 600 - (first_weight + second_weight)
print('현재 엘리베이터에 허용무게는 {:.2f}kg 입니다.'.format(weight))