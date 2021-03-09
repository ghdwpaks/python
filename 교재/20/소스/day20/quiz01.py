# 커피의 개당 가격은 2000원, 10개 초과하면 초과하는 양에 대해서만
# 개당 1500원씩 받는다.커피의 개수를 입력 받아 금액을 반환하는 함수

# 과자 1개에 1000원, 한 번에 10개 이상을 사면 전체 금액의 10 % 할인
# 그리고 100개 이상을 사면 전체 금액의 12 % 할인한다. 개수를 입력 받아서
# 금액을 구해 반환하는 함수를 만들어주세요.
def coffee(cnt) :
    cost = 2000 * cnt
    if cnt > 10 :
        cost = (cnt - 10) * 1500 + 20000
    return cost

def snack(cnt) :
    cost = 1000 * cnt
    if cnt >= 100 :
        cost = int(cost * 0.88)
    elif cnt >= 10 :
        cost = int(cost * 0.9)

    return cost 

print( coffee(10) )
print( coffee(11) )
print( coffee(12) )
print()
print( snack(9) )
print( snack(10) )
print( snack(100) )