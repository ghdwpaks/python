# 1. numbers = (10, 20, 30, 40, 50, 60, 70)
#    위 튜플 자료에서 30과 40을 따로 num1, num2 변수에 할당 하시오.
numbers = (10, 20, 30, 40, 50, 60, 70)
num1, num2 = numbers[2:4]
print('num1 : {}, num2 : {}'.format(num1, num2))
print()
# 2. tuple_data = 10, 20, "tuple", 1.123, 'string‘
#    위 데이터를 리스트 변수에 넣으시오.
tuple_data = 10, 20, "tuple", 1.123, 'string'

list_data = tuple_data
print(type(list_data))
print(list_data)

list_data = list(tuple_data)
print(list_data)
print(type(list_data))

# 3. menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))
#    위 자료의 값을 다음의 양식 처럼 출력 하시오.
#    칼국수 - 6,000원
#    비빔밥 - 5,500원
#    돼지국밥 – 7,000원
print()
menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000))
for title, price in menu :
    print('{} - {:,}원'.format(title, price))