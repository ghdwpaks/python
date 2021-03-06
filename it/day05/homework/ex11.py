print("Hello world!")

work = []
while(True) :
    in1 = input("당신이 오늘 해야할 일들은?\n>>")
    if(in1 == "exit" ) :
        break
    work.append(in1)

if "빨래" in work :
    print("당신의 오늘 할일들중, 빨래가 있네요!")
