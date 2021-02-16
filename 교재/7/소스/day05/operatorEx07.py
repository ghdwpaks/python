
# 비트 연산자
data1 = 3
data2 = 5
'''
or 연산은 두 개의 데이터 중 한 개라도 1이 있다면 결과가 1
두 개의 데이터 모두 0이면 결과도 0
data1 | data2
0011 (3)
0101 (5)
---------
0111 (7)
'''
result = data1 | data2
print('{} | {} = {}'.format(data1, data2, result))

'''
and 연산은 두 개의 데이터 중 한 개라도 0이 있다면 결과가 0
두 개의 데이터 모두 1이면 결과도 1
data1 & data2
0011 (3)
0101 (5)
---------
0001 (1)
'''
result = data1 & data2
print('{} & {} = {}'.format(data1, data2, result))

'''
같은 데이터끼리 XOR의 결과는 0, 
다른 데이터끼리 XOR의 결과는 1
data1 ^ data2
0011 (3)
0101 (5)
---------
0110 (6)
'''
result = data1 ^ data2
print('{} ^ {} = {}'.format(data1, data2, result))


