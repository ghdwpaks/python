print("Hello world!")
in1 =""
pay = []
while(True) :
    in1 = input("당신이 지출해야하는 것들의 금액은?\n>>")
    if(in1 == "exit" ) :
        break
    in1 = int(in1)
    pay.append(in1)
sum_all = sum(pay)
print("당신의 지출 총액은 {}원입니다!".format(sum_all))
