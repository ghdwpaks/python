data1 = 100
data2 = '100'
data3 = '1.1111'
'''
위 변수들을 사용해서 아래와 같이 출력하시오.
'''
#200
print(data1 + int(data2))
#101.1111
print(data1 + float(data3))
#100100
print(str(data1) + data2)
