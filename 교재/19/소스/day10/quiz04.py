# 1에서 1000까지의 자연수중에서 4로 나누어도 6으로 나누어도 
# 나머지가 1인 수의 합을 출력하라.(합계 : 41916)

total = 0
for i in range(1, 1001) : 
    if i % 4 == 1 and i % 6 == 1 :
        total += i
print('합계 : {:,}'.format(total))

# 첫날에 1원을 예금하고, 다음날에는 전날의 2배씩 증가하는 방식이다. 
# 30일째 되는날 예금해야하는 금액을 구하시오

total = 0; seed = 1
for i in range(1, 31) : 
    total += seed
    seed *= 2
print('저축 금액 : {:,}원'.format(total))

# 전설에 따르면 체스 발명자는 왕으로부터 받을 상을 말하도록 
# 요구 받았을 때 발명자가 말하길 체스 판의 
# 첫 번째 사각형에는 밀알을 1개, 두 번째 사각형에는 밀알을 2개, 
# 세 번째 사각형에는 밀알을 4개 등으로 총 64칸에 밀알을 2배씩 
# 채워주기를 요구했다. 이 발명가가 요구한 밀알의 총 개수는?

total = 0; seed = 1
for i in range(1, 65) : 
    total += seed
    seed *= 2
print('밀알 : {:,}개'.format(total))



