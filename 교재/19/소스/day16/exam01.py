tuple_data1 = 10,20,30
tuple_data2 = (40,50,60)

print(tuple_data1)
print(tuple_data2)
print('자료형 : ', type(tuple_data1))
print('자료형 : ', type(tuple_data2))
print('자료형 : ', type(tuple_data1[0]))

# 아래 코드는 에러 발생, tuple 자료형의 변수이기에 데이터 변경 불가
#tuple_data1[0] = 100
