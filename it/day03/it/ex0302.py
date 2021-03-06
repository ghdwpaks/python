'''
변슈 자료형 변환에 관하여
자료형을 변환시키기 위한 함수는 다음과 같다
int()   정수형 자료로 변환
str()   문자열 자료로 변환
float() 실수형 자료로 변환
'''
var1, var2, var3 = '1',1,1.0
var1, var2,var3 = int(var1),float(var2),str(var3)

print("{}".format(type(var1)))
print("{}".format(type(var2)))
print("{}".format(type(var3)))
print()


data1 = '123'
print("data1({}) : {}".format(data1,type(data1)))
data1 = int(data1)
print("data1({}) : {}".format(data1,type(data1)))
data1 = float(data1)
print("data1({}) : {}".format(data1,type(data1)))
data1 = str(data1)
print("data1({}) : {}".format(data1,type(data1)))


