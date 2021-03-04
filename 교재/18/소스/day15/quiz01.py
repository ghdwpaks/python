'''
numbers = [10, 20, 30, 40, 50, 60, 70]
  위 리스트의 모든 값을 더한 결과를 출력 하시오.

1 ~ 45 까지 임의의 값을 중복 없이 6개 생성하여 출력하는 
코드를 작성 하시오.

listData = [['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28]]
  위의 2차 리스트 자료를 다음과 같은 형식으로 출력 하시오.

      이름 : 홍길동
      성별 : 남
      나이 : 36
'''
import random

numbers = [10, 20, 30, 40, 50, 60, 70]
total = 0

for i in numbers :
    total += i
print('{}의 합계 : {}'.format(numbers, total))
print()
numbers = []
count = 0
while True :
    tmp = random.randrange(1,46)
    if tmp not in numbers :
        numbers.append(tmp)
        count += 1
    if count == 6:
        break

print('중복 없는 6개의 랜덤 데이터 : ', numbers)
print()
listData = [ ['홍길동', '남', 36], ['김수양', '여', 32], ['박담소', '남', 28] ]
for ld in listData :
    print('이름 : ',ld[0])
    print('성별 : ',ld[1])
    print('나이 : ',ld[2])
    print()