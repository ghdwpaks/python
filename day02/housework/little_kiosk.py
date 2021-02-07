print("Hello world!")

print("지금 이 자판기에서는\n1.콜라\n2.사이다\n3.환타\n4.오렌지주스\n5.레몬에이드\n들을 판매하고있습니다.")
#coke = 1000
#soda = 1100
#fanta = 1200
drink_list = []
drink_list.append(1000)
drink_list.append(1100)
drink_list.append(1200)
drink_list.append(1300)
drink_list.append(1400)

for i in range (0 , 5) :
    print(drink_list[i])



print("얼마를 넣으실건가요?\n>>",end="")
input_cost = int(input())

while True:
    print("무엇을 고르실건가요?\n>>",end="")
    input_kind = str(input())
    if input_kind == '1' or input_kind == "콜라":
        input_kind = "콜라"
        cost = drink_list[0]
        break
    elif input_kind == '2' or input_kind == "사이다": 
        input_kind = "콜라"
        cost = drink_list[1]
        break
    elif input_kind == '3' or input_kind == "환타": 
        input_kind = "콜라"
        cost = drink_list[2]
        break
    elif input_kind == '4' or input_kind == "오렌지주스":
        input_kind = "오렌지주스"
        cost = drink_list[3]
    elif input_kind == '5' or input_kind == "레몬에이드":
        input_kind = "레몬에이드"
        cost = drink_list[4]
        

if input_cost < cost :
    print("금액이 부족하여 음료수를 제공할 수 없습니다.")
else :
    print("주문하신"+input_kind+"가 나왔습니다.")
    print("거스름돈은",(int(input_cost)-cost),"원 입니다.")






