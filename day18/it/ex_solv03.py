'''
input() 함수로 입력 받은 더하기, 빼기, 곱하기, 나누기의
간단한 수식을 처리 할 수 있도록 코드를 작성하시오
'''
while True :
    exp = input("입력 :")
    if '+' in exp :
        x = "+"
        data1,data2 = exp.split('+')
        data1 = int(data1.strip())
        data2 = int(data2.strip())
        total = data1 + data2
    elif '-' in exp :
        x = "-"
        data1,data2 = exp.split('-')
        data1 = int(data1.strip())
        data2 = int(data2.strip())
        total = data1 - data2
    elif '*' in exp :
        x = "*"
        data1,data2 = exp.split('*')
        data1 = int(data1.strip())
        data2 = int(data2.strip())
        total = data1 * data2
    elif '/' in exp :
        x = "/"
        data1,data2 = exp.split('/')
        data1 = int(data1.strip())
        data2 = int(data2.strip())
        total = data1 / data2
    else :
        print("입력 값을 확인 하세요")

    print("{} {} {} = {}".format(data1,x,data2,total))




