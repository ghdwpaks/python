# python, c_language, java 3과목의 점수를 변수에 넣어주고
# 합계와 평균을 구하는 프로그램을 작성하시오.(소수점 2자리) 
python = 100
c_language = 80
java = 77
sum_data = python + c_language + java
avg_data = sum_data / 3

print('python({}) + c_language({}) + java({})'
.format(python, c_language, java))
print('합계 : {}, 평균 : {:.2f}'.format(sum_data, avg_data))
