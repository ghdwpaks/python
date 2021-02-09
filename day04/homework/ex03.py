print("hello world!")

work = []

while(True) :
    userans = input("당신의 오늘 할일은 무엇이 있습니까?\n>>")
    if(userans == "exit") :
        break
    work.append(userans)


print("당신의 할일은")
for i in work : print(i)
print("(들)이 있습니다.")

