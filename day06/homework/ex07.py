print(10)

d = 10
print(d)

'''
한글사용 가능하지만 웬만하면 정말 쓰지 않는것을 권장하며
대부분 알파벳, 숫자, 언더스코어(언더바)로 구성
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
print('실수 변수 :', float_data)
print('실수 변수 : %.2f' % float_data)
print('실수 변수 : {:.2f}'.format(float_data))


float_data = float_data + 1.11
print("실수 변수 : {:.2f}".format(float_data))

string_data = "문자열"
print("문자열(str) 변수 :",string_data)
print("문자열(str) 변수 : %s" % string_data)
print("문자열(str) 변수 : {}".format(string_data))

string_data = string_data + '문자열2'
print("문자열(str) 변수 : {}".format(string_data))