# 1에서 1000사이 자연수중에 수를 구성하는 개개의 수가 
# 서로 연속적으로 되어 있는 수를 찾아 출력하는 프로그램을 작성하세요
# ex) 11, 22, 33, 44, …, 999

for i in range(1, 1001):
    data1 = i % 10
    data2 = i // 10 % 10
    data3 = i // 100
    if data1 == data2 and data3 == 0 :
        print('{} '.format(i), end='')
    if data1 == data2 and data1 == data3 :
        print('{} '.format(i), end='')