'''
쌀 102통(1통 = 1KG)이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다.
쥐 한마리가 하루에 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다.
며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까?
그리고 쥐는 총 몇 마리 인가?
'''
g = 1000 #1kg
rice = g * 102 #쌀 총량(g)
d = 20  #하루 소비
rat = 2 #쥐 수
dc = 0 #day count 소비 날짜

while True :
    rice = rice - (rat * d)
    if rice < 0 :
        break
    dc += 1
    rat *= 2
print("경과한 날짜 :",dc)
print("최중 쥐 수:",rat)
    
'''선생님 답안'''

rice = 102 * 1000
mouse = 2
day = 0
while True :
    day += 1
    rice = rice - (mouse * 20)
    if day % 10 == 0 :
        mouse *= 2
    if rice <= 0 :
        break
print("{}일 {}마리 {}g".format(day,mouse,rice))






