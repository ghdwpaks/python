#랜덤 데이터 만들기
import random

# 범위 1~45 
# i = 1
# while i <= 5 :
#     print('{}번째 랜덤 : {}'.format(i, int(random.random() * 45) + 1))
#     i += 1

# 범위는 1 ~ 2 
i = 1
while i <= 5 :
    print('{}번째 랜덤 : {}'.format(i, random.randrange(1,3)))
    i += 1

# 1 ~ 45
for i in range(6, 11) :
    print('{}번째 랜덤 : {}'.format(i, random.randrange(1,46)))