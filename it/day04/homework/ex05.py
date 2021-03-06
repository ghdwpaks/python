print("Hello world!")

gamemode = ['survival','creative','watching']
user_gamemode = 0

while(True) :
    print("현재의 게임모드는 {}입니다.".format(gamemode[user_gamemode]))

    user_gamemode = int(input("게임모드를 몇번으로 변경하시겠습니까?\n>>"))
