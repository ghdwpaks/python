#랜덤 데이터 만들기
# 범위 0.0 ~ 1.0 미만
import random

i = 1
while i <= 5 :
    print('{}번째 랜덤 : {}'.format(i, random.random() ))
    i += 1

while i <= 10 :
    print('{}번째 랜덤 : {}'.format(i, random.random() * 10 ))
    i += 1

# int(random.random() * 10 ) : 0 ~ 9 범위
# 1 ~ 10
while i <= 15 :
    print('{}번째 랜덤 : {}'.format(i, int(random.random() * 10 ) + 1))
    i += 1