import os

stop = True
sum = avg = name = ''

while stop :
    print('='*20)
    print('{:^20}'.format('M e n u'))
    print('='*20)
    print('1. 학생이름 입력')
    print('2. 성적 3과목 입력')
    print('3. 학생이름 출력')
    print('4. 합계 출력')
    print('5. 평균 출력')
    print('6. 종료')
    print('='*20)
    select = int(input('>> '))
    if select == 1:
        name = input('학생 이름 : ')
        print('학생 이름 입력 완료되었습니다.')
    elif select == 2:
        kor = int(input('국어 점수 입력 : '))
        eng = int(input('영어 점수 입력 : '))
        math = int(input('수학 점수 입력 : '))
        sum = kor + eng + math
        avg = sum / 3
        print('과목 점수 입력 완료되었습니다.')
    elif select == 3:
        if name != '' :
            print('이름 : {}'.format(name))
        else :
            print('이름을 입력 후에 다시 실행하세요.')
    elif select == 4:
        if sum != '' :
            print('합계 : {}'.format(sum))
        else :
            print('3과목의 성적을 입력 후에 다시 실행하세요.')
    elif select == 5:
        if sum != '' :
            print('평균 : {:.2f}'.format(avg))
        else :
            print('3과목의 성적을 입력 후에 다시 실행하세요.')
    elif select == 6 :
        stop = False
    else :
        print('메뉴를 확인 후 다시 입력하세요')
    os.system('pause')
    os.system('cls')