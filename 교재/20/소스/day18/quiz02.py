# input() 함수로 이름과 나이 값을 입력 받을 때 
# 한 번에 입력 받아 처리하고 출력 하는 코드를 작성 하시오.
# ex) 입력 : 김변수 20

name, age = input('입력 : ').split(' ')
print('이름 : {}, 나이 : {}'.format(name, age))

# input() 함수로 입력 받은 더하기, 빼기, 곱하기, 나누기의 
# 간단한 수식을 처리 할 수 있도록 코드를 작성 하시오.
# ex) 입력 : 1 + 1
# ex) 입력 : 1+1
# ex) 출력 : 2
total = 0 
exp = input('입력 : ')
if '+' in exp :
    idx = exp.find('+')
    oper = exp[idx]
    data1, data2 = exp.split('+')
    data1 = int(data1.strip())
    data2 = int(data2.strip())
    total = data1 + data2
elif '-' in exp :
    idx = exp.find('-')
    oper = exp[idx]
    data1, data2 = exp.split('-')
    data1 = int(data1.strip())
    data2 = int(data2.strip())
    total = data1 - data2
elif '*' in exp :
    idx = exp.find('*')
    oper = exp[idx]
    data1, data2 = exp.split('*')
    data1 = int(data1.strip())
    data2 = int(data2.strip())
    total = data1 * data2
elif '/' in exp :
    idx = exp.find('/')
    oper = exp[idx]
    data1, data2 = exp.split('/')
    data1 = int(data1.strip())
    data2 = int(data2.strip())
    total = data1 / data2
else :
    print('입력 값을 확인 하세요')

print('{} {} {} = {}'.format(data1, oper, data2, total))
