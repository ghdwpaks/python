'''
터미널에 출력을 다음과 같이 출력하세요
10,20,30 은 변수의 데이터를 출력
num1(10) + num2(20) = 30
'''
num1 = 10 ;num2 = 20;num3 = num1+num2
print('num1(10) + num2(20) = {}'.format(num3))
print('num1(%d) + num2(%d) = %d'%(num1,num2,num3))