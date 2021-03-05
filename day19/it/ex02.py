'''
사용자 정으 ㅣ함수
1. 특정 코드를 재 사용할 수 있다.
2. 반복적으로 작성 코드를 하나의 함수로 정의 할 수 있다
3. 개발 시에 기능별로 나누어서 개발기간을 단축 시킬 수 있다.
4. 1~2번 방식을 통해 가독성을 높일 수 있다.


사용방법 :
def 함수 이름(매개변수들) :
    실행할 코드

근데 '매개변수들'은 선택사항이다.
'''

def func1() :
    print("Hello")

def func2() :
    data1 = 10
    data2 = 20
    return data1 + data2
def func3(data1) :
    data2 = 20
    return data1 + data2
def func4(data1,data2) :
    return data1 + data2

def func5(data1,data2) :
    if data1 == None :
        data1 = 0
    if data2 == None :
        data2 = 0
    return data1 + data2

#print(func5())




