'''
python, c_language, java 3과목의 점수를 변수에 넣어주고
합계와 평균을 구하는 프로그램을 작성하시오(소수점2자리)
'''
score_py = 100
score_c = 90
score_java = 80
sum_all = score_c + score_py + score_java
ave = sum_all / 3
print("score_py = {}".format(score_py))
print("score_c = {}".format(score_c))
print("score_java = {}".format(score_java))
print()

print("파이썬(python)\t\t과목 점수 = {}".format(score_py))
print("C언어(C_language)\t과목 점수 = {}".format(score_c))
print("자바(Java)\t\t과목 점수 = {}".format(score_java))
print()

print("합계 : {}".format(sum_all))
print("평균 : {}".format(ave))
print()
print()

'''선생님 풀이'''
python = 100
c_language = 80
java = 70
sum_data = python + c_language + java
avg_data = sum_data / 3
print('python({}) + c_language({}) + java({}) = sum({})'.format(python,c_language,java,sum_data))
print('python(%d) + c_language(%d) + java(%d) = sum(%d)' % (python,c_language,java,sum_data))

print('합계 : {}, 평균 : {:.2f}'.format(sum_data,avg_data))

