print("Hello world!")

print("지난 일주일동안 게임을 몇시간 했는지 입력하세요.")
userans1 = input()
userans1 = int(userans1)
DayPlayTime = userans1 // 7
print("당신은 지난주중, 하루에 평균 약{}시간을 플레이하였습니다.".format(DayPlayTime))