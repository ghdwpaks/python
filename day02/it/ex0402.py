print("%s님의 나이는 %d입니다." % ('김변수',39))
print("{}님의 나이는 {}입니다.".format("이상수",29))
print()

#float, 소수점을 포함하는 실수형식의 변수는 대부분 소수점6번째까지 출력한다.
print('%s님의 몸무게는 %f입니다.'%('김변수', 77.7))
print('{}님의 나이는 {:f}입니다.'.format('이상수',66.6))
print()
'''
근데 굳이 소수점 6번째까지 출력할 필요가 없거나
더 자세하게 소수점 6번째 이상까지 출력할 필요가 있는 경우에는
아래와같이 입력해서 몇번째 소수점까지 출력할것인지 결정할 수 있다.
'''
print('%s님의 몸무게는 %.2f입니다.'%('김변수', 77.7))
print('{}님의 나이는 {:.1f}입니다.'.format('이상수',66.6))

print('%10d원'%(1000))
print('%10d원'%(100000))
print('{:10}원'.format(100000))
print('{:10}원'.format(10000000))

#이런식으로 숫자 뿐만이 아니라 문자 및 문자열 또한 왼쪽, 오른쪽 , 가운데 정렬을 할 수 있다.
print('%10s, %-10s'%('오른쪽','왼쪽'))
print('{:>10}, {:<10}'.format('오른쪽','왼쪽'))
print("{:^10}".format('가운데'))
'''
근데 위에처럼 굳이 -(마이너스)를 넣거나 빼지 않아도 
오른쪽정렬을 할거면 %숫자d,
왼쪽정렬을 할거면 %0숫자d,

오른쪽정렬을 할거면 {:숫자},
왼쪽정렬을 할거면 {:0숫자},
'''
print("%5d %05d" % (10,100))
print("{:5} {:05}".format(100, 12))

#추가로, 이것은 정렬에 관한것은 아니지만 밑에처럼 입력하게 되면 3자리를 넘어가게 될때마다 ,를 붙혀준다.
print("{:,}".format(10000000))
#이 방법은 {:,}으로 쓰는게 편하고, %d같이 %를 쓰는 방식으로는...반복문을 돌려서 일일이 넣는 불편한 방법.