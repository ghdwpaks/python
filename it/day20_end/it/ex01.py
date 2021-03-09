'''
커피의 개당 가격은 2000원, 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다. 커피의 개수를 입력 받아 금액을 반환하는 함수

'''

def cal_coffee_cost(count) :
    if count <= 10 :
        return count*2000
    elif count > 10 :
        return (10 * 2000) + count * 1500
while True :
    u = int(input("커피를 몇잔 드시겠습니까? : "))
    res = cal_coffee_cost(u)
    print("가격은 {}원 입니다!".format(res))


'''선생님 답안'''
def coffee(cnt) :
    cost = 2000 * cnt
    if cnt > 10 :
        cost = (cnt - 10) * 1500 + 20000
    return cost




