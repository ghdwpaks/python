'''
 동전 게임
 앞면 / 뒷면 맞추기 
 소스 -> day14 -> 동전 게임.exe 

 컴퓨터는 랜덤 값을 1 or 2를 갖도록 만든다.
 사용자의 값을 입력받아 1은 동전의 앞면, 2는 동전의 뒷면으로
 컴퓨터의 랜덤 값이 서로 같다면 '맞췄습니다'를 출력
 랜덤 값이 서로 다르다면 '틀렸습니다'를 출력하시오.
  == 동전 앞/뒤 맞추기 ==
  1.앞면 / 2.뒷면 / 3.종료
  선택 > 1
  틀렸습니다.

  == 동전 앞/뒤 맞추기 ==
  1.앞면 / 2.뒷면 / 3.종료
  선택 > 1
  맞췄습니다!
'''
import random
import os
while True :
    print('== 동전 앞/뒤 맞추기 ==')
    print('1.앞면 / 2.뒷면 / 3.종료')
    select = int(input('선택 > '))
    com = random.randrange(1, 3)

    if select == 3 :
        print('동전 게임을 종료합니다.')
        break
    if 0 < select and select < 3 :
        if com == select :
            print('맞췄습니다.')
        else :
            print('틀렸습니다.')
    else :
        print('메뉴를 확인 후 다시 입력하세요')
    os.system('pause')
    os.system('cls')
