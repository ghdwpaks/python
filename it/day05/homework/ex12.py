print("Hello world!")

work = []
while(True) :
    in1 = input("당신이 오늘 해야할 일들은?\n>>")
    if(in1 == "exit" ) :
        break
    work.append(in1)

if "코딩" not in work :
    print("오늘은 왜 코딩을 안하는거죠...?")