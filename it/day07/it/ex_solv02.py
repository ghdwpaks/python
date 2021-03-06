print("Hello world!")

in1 = int(input("커피를 몇개 주문하시겠습니까?"))

od = 0
over = 0
if in1 > 10 :
    od = 10
    over = in1 - 10

cost = (od * 2000) + (over * 1500)

print("구매비용은 {}원입니다!".format(cost))

print("\n\n\n분기점\n\n\n")

'''선생님 풀이'''
coffee = int(input('커피 개수 입력 : '))
cost = 0
if coffee > 10:
    cost = 20000 + (coffee - 10) * 1500
elif coffee <= 0:
    cost = 0
else :
    cost = coffee * 2000
print("{}잔은 {}원입니다.".format(coffee,cost))





