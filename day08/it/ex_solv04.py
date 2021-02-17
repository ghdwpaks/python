'''
정수를 입력 받아 아래와 같이 출력하시오.

1) 3의 배수이면서, 4의 배수에도 해당 => []은(는) 3의 배수이면서, 4의 배수입니다.
2) 3의 배수에만 해당 => []은(는) 3의 배수입니다.
3) 4의 배수에만 해당 => {}은(는) 4의 배수입니다.
4) 3의 배수도, 4의 배수도 해당 안됨 => []은(는)3의 배수도, 4의 배수도 아닙니다.
5) (0입력시, 잘못입력)
========>입력받은 값에 따라 출력 되게 만드세요.<=======
'''

i = int(input("정수 입력"))
k3 = False
k4 = False

if i % 3 == 0 :
    k3 = True
if i % 4 == 0 :
    k4 = True
if i <= 0 :
    print("잘못 입력하셨습니다.")
else :
    if k3 and k4 :
        print("{}은(는) 3의 배수이면서, 4의 배수입니다.".format(i))
    elif k3 :
        print("{}은(는) 3의 배수입니다.".format(i))
    elif k4 :
        print("{}은(는) 4의 배수입니다.".format(i))
    else :
        print("{}은(는) 3의 배수도, 4의 배수도 아닙니다.".format(i))

'''선생님 답안'''
data = int(input("입력 : "))
print_data = ''
if data == 0 :
    print_data = "{}은(는) 잘 못 입력".format(data)
elif data % 3 == 0 and data % 4 == 0 :
    print_data = '{}은(는) 3의 배수이면서, 4의 배수입니다.'.format(data)
elif data % 3 == 0  :
    print_data = '{}은(는) 3의 배수입니다'.format(data)
elif data % 4 == 0 :
    print_data = '{}은(는) 4의 배수입니다.'.format(data)
else :
    print_data = '{}은(는) 3의 배수도, 4의 배수도 아닙니다.'.format(data)

print(print_data)


