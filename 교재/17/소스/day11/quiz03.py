# 쌀 102통(1통 == 1KG)이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다.
# 쥐 한마리가 하루에 20g씩의 쌀을 먹고, 10일(10,20,30)마다 쥐의 수가 2배씩 증가한다. 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까. 그리고 쥐는 총 몇 마리 인가?

rice = 102 * 1000
mouse = 2
day = 0
while True : 
    day += 1
    rice = rice - (mouse * 20)
    print(rice)
    if day % 10 == 0 :
        mouse *= 2
    if rice <= 0 :
        break

print('{}일 {}마리 {}g'.format(day, mouse, rice))
