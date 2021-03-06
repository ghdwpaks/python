'''
과자 1개에 1000원, 한번에 10개 이상을 사면 전체 금액의 10% 할인 그리고 100개 이상을 사면 전체 금액의 12%할인한다. 개수를 입력 받아서 금액을 계산 하는 프로그램 작성
'''

print("Hello world!")

b = int(input("과자 구매 갯수 : "))
c = b * 1000
dc = 0
if b >= 100 :
    dc = (c // 100) * 12
elif b >= 10 :
    dc = c // 10


c -= dc
print("가격은 {}원 입니다.".format(c))

'''선생님 풀이'''
snack = int(input("과자 개수 입력 : "))
cost = snack * 1000
if snack <= 0 :
    cost = 0
elif snack >= 100 :
    cost = cost * 0.88
elif snack >= 10 :
    cost = cost * 0.9

print("과자 {}개는 {:,}원 입니다.".format(snack,cost))







