'''
1.입력된 수의 각 자리수의 합을 구하는 프로그램을 작성하라

2. 입력된 수를 거꾸로 정수형 변수에 담아 출력하시오.
'''

in1 = input("정수 입력 : ")
summ1 = 0
for i in range(0 , len(in1)) :
    summ1 += int(in1[i])
print("summ1 =",summ1)

in2 = int(input("정수 입력 : "))
while True :
    mod = in2  % 10
    print("{}".format(mod),end="")
    in2  = in2  // 10
    if in2  == 0 :
        break

'''선생님 답안'''

while True :
    data = int(input('입력 : '))
    if data >= 1 and data <= 100 :
        break
    else :
        print('1~100사이의 값을 입력해주세요.')

i = 1; total = 0
while i <= data :
    total += i
    i += 1
print('1 ~ {}의 합계 : {}'.format(data ,total))


