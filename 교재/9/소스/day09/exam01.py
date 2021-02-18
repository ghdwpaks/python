
# while 조건식 : 
#     종속문장1
#     종속문장2
#     종속문장3
# 다음 문장

loop_flag = True
while loop_flag :
    data = input('입력 : ')
    print('입력 데이터는 {}입니다.'.format(data))
    if data == '종료' :
        loop_flag = False

loop_count = int(input('반복 횟수 : '))
i = 1
while i <= loop_count :
    print('{}번째 반복'.format(i))
    i += 1
