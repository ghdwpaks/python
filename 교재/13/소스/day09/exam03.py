'''
반복문
 - for문
 - while문

 for 변수 in 집합 :
     종속문장1
     종속문장2
     종속문장3
집합 : range(), 리스트, 튜플, 문자열
'''

# range(10) : 0 ~ 9까지 10번
# range(1,10) : 1 ~ 9까지 9번
# range(1,10,2) : 1,3,5,7,9 
for i in range(10) :
    print('{}번째 반복'.format(i))
print()
for i in range(1, 10, 3) :
    print('{}번째 반복'.format(i))
