# 비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 
# 10분 단위로 추가요금 5000원씩 부가된다.
# 비행기 탈 시간을 입력하여 요금 계산기를 만드시오.
time = int(input('비행기 이용시간(분) : '))
time -= 30

if time <= 0 :
    cost = 30000
elif time % 10 == 0 : # 40, 50, 60...즉 10의 배수들의 분에 대한 요금 구하는 코드
    cost = 30000 + (time // 10) * 5000
else : # 일의 자리에 값이 1~9에 해당하는 분에 대한 요금을 구하는 코드
    cost = 30000 + (time // 10 + 1) * 5000

time += 30
print('비행기 이용시간은  {}분으로 요금은 {:,}원입니다.'.format(time, cost))

# 과자 1개에 1000원, 한 번에 10개 이상을 사면 전체 금액의 10%할인 
# 그리고 100개 이상을 사면 전체 금액의 12%할인한다. 개수를 입력 받아서 
# 금액을 계산하는 프로그램 작성
snack = int(input('과자 개수 입력 : '))

cost = snack * 1000
if snack <= 0 :
    cost = 0
elif snack >= 100 :
    cost = cost * 0.88
elif snack >= 10 :
    cost = cost * 0.9

cost = int(cost)
print('과자 {}개는 {:,}원 입니다.'.format(snack, cost))
