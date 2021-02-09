#두 수를 입력받아 합계를 출력하시오.

i1 = int(input())
i2 = int(input())
print("두 수의 합계 : " , i1 + i2)

'''선생님 풀이'''

data1 = input('입력 : ')
data2 = input('입력 : ')
sum_data = int(data1) + int(data2)
print('data1({}) + data2({})의 합계 : {}'.format(data1,data2, sum_data))

#추가코드
data1 , data2 = input('두 수 입력 : ').split() #split() 공백을 기준으로 문자열 처리 및 분리
print("{} + {} = {}".format(data1,data2,sum_data))