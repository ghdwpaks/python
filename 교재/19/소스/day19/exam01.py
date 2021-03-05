'''
사용자 정의 함수
1. 특정 코드를 재 사용할 수 있다.
2. 반복적으로 작성 코드를 하나의 함수로 정의할 수 있다.
3. 개발 시에 기능별로 나누어서 개발기간을 단축 시킬 수 있다.
4. 1~2번을 통해 가독성을 높일 수 있다.

def 함수이름() :
    실행할 코드

def 함수이름() :
    실행할 코드
    return 데이터

def 함수이름(매개변수1 ) :
    실행할 코드

def 함수이름(매개변수1, 매개변수2.... ) :
    실행할 코드

'''

def func01() :
    print('hello func01')

def func02() :
    data1 = 10
    data2 = 20
    print('hello func02')
    return data1 + data2

def func03(data1) :
    data2 = 20
    print('hello func03')
    return data1 + data2

def func04(data1, data2) :
    print('hello func04')
    return data1 + data2

func01() #함수호출
func02() 
func03(3) # 매개변수에 데이터를 전달한다.
func04(4, 5)

print('func01() : ', func01())
print('func02() : ', func02())
print('func03() : ', func03(3))
print('func04() : ', func04(4,5))

