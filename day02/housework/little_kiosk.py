print("Hello world!")

print("지금 이 자판기에서는\n1.콜라\n2.사이다\n3.환타\n들을 판매하고있습니다.")
coke = 1000
soda = 1100
fanta = 1200
print("얼마를 넣으실건가요?\n>>",end="")
input_cost = int(input())

while True:
    print("무엇을 고르실건가요?\n>>",end="")
    input_kind = str(input())
    if input_kind == '1' or input_kind == "콜라":
        input_kind = "콜라"
        cost = coke
        break
    elif input_kind == '2' or input_kind == "사이다": 
        input_kind = "콜라"
        cost = soda
        break
    elif input_kind == '3' or input_kind == "환타": 
        input_kind = "콜라"
        cost = fanta
        break


if input_cost < cost :
    print("금액이 부족하여 음료수를 제공할 수 없습니다.")
else :
    print("주문하신"+input_kind+"가 나왔습니다.")
    print("거스름돈은",(int(input_cost)-cost),"원 입니다.")






