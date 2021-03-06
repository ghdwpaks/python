menu = (('칼국수',6000),('비빔밥',5500),('돼지국밥',7000))

for i in range(0,len(menu)) :
    print("{} - {}원".format(menu[i][0],menu[i][1]))



print("\n\n\n분기점\n\n\n")
'''선생님 답안'''

for title,price in menu :
    print('{} - {:,}원'.format(title,price))


