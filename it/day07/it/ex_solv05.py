print("Hello world!")
'''
학점을 입력 받아 구문하여 문자열 출력
입력 데이터는 문자 A부터 F
A 와 B는 "참 잘했어요"
C 와 D는 "분발합시다."
F는 아무것도 출력하지 않는다.
'''


g = input('학점 : ')
if g == 'A' or g == "B" :
    print("참 잘했어요.")
elif g == 'C' or g == 'D' :
    print("분발합시다.")



'''선생님 답안'''
grade = input("학점 입력 : ")
print_string = ''

if grade == 'A' or grade == "B" :
    print_string = "참 잘했어요."
elif grade == "D" or grade == "D" :
    print_string = '분발합시다.'
print("{}학점은 {}".format(grade,print_string))










