print("Hello world!")
gm = []
gm.append("combat")
gm.append("create")
gm.append("drive")
gm.append("broke")
gm.append("fly")
gm.append("swim")

print("게임모드는 다음과 같이 있습니다.!")
for i in gm : print(i)
print()
while(True) :
    userans = input("어떤 모드를 플레이하시겠습니까?\n>>")
    if userans == "combat" :
        gm_n = 0
    elif userans == "create" :
        gm_n = 1
    elif userans == "drive" :
        gm_n = 2
    elif userans == "broke" :
        gm_n = 3
    elif userans == "fly" :
        gm_n = 4
    elif userans == "swim" :
        gm_n = 5

    print("현재의 모드는 {}입니다!".format(gm[gm_n]))

