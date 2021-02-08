#변수명 = 값
#변수명1 , 변수명2 = 값1,값2
#변수명1 = 변수명2 = 값

print(10)
data = 10
print(data)
data2 = 20
print("data : ",data)
print("dtat2 : ",data2)

intdata = 100
intData = 110
print("intData :",intData)
print("intdata :",intdata)
#대소문자 구분함
'''
한글사용 가능하지만 웬만하면 정말 쓰지 않는것을 권장하며
대부분 알파벳, 숫자, 언더스코어(언더바)로 구성됨

변수명의 시작은 숫자로 할 수 없으며
int, str같이 python  내부의 명령어나 예약어를 사용할 수도 없음
공백이나 특수기호(!,@,$등등)는 포함할 수 없음
'''

smallData = 2   #camel 형식 네이밍
small_data = 3  #snake 형식 네이밍
SmallData = 4   #CapWord 형식 네이밍

data = 100
print('정수형변수 :',data)
print('정수형변수 : %d'%data)
print('정수형변수 : {0}'.format(data))

data = data + 100
print("정수형 변수 : {}",format(data))


float_data = 3
print('실수형 변수 :', float_data)
print('실수형 변수 : %.2f' % float_data)
print('실수형 변수 : {:.2f}'.format(float_data))


float_data = float_data + 1.11
print("실수형 변수 : {:.2f}".format(float_data))

string_data = "문자열"
print("문자열 변수 :",string_data)
print("문자열 변수 : %s" % string_data)
print("문자열 변수 : {}".format(string_data))

string_data = string_data + '문자열2'
print("문자열 변수 : {}".format(string_data))

'''
1.정수 :    0과 음수, 양수 값을 표함한 숫자 값
2.실수 :    소수점을 사용하는 숫자 값
3.문자열 :  따옴표로 묶여 있는 값
4.리스트 :  정수, 실수 및 문자열 등 자료들의 집합(값의 집합)
5.튜플 :    정수, 실수 및 문자열 등 자료의 집합(값의 집합)
6.사전 :    정수 , 실수 및 문자열 등 자료들의 집합(키와 값이 쌍으로 존재)
'''

#type()함수는 변수의 데이터 자료형을 파악하는 용도로 사용된다
data1, data2, data3 = 1, 1.1 , '문자열'
print("{}".format(type(data)))
print("{}".format(type(data1)))
print("{}".format(type(data2)))
print("{}".format(type(data3)))
print()

print("{}".format(type(data1)))
data1 = 2.2
print("{}".format(type(data1)))
data1 = 'string'
print("{}".format(type(data1)))