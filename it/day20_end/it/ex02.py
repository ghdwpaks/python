'''
과자 1개에 1000원, 한번에 10개 이상을 사면 전체 금액의 10%할인 그리고 100개 이상을 사면 전체 금액의 12%를 할인한다. 개수 입력 받아서 금액을 구해 반환하는 함수를 만들어주세요.


'''

def cal_snack_cost(count) :
    if count < 10 :
        return count * 1000
    elif count < 100 :
        return count * 1000 - (count * 1000) // 10
    elif count >= 100 :
        return count * 1000 - ((count * 1000) // 100) * 12
while True :
    u = int(input("구입하실 과자의 갯수는? : "))
    res = cal_snack_cost(u)
    print("과자 금액의 총 합산은 {}원 입니다!".format(res))

'''선생님 답안'''
def snack(cnt) : 
    cost = 1000 * cnt
    if cnt >= 100 :
        cost = cost * 0.88
    elif cnt >= 10 :
        cost = cost * 0.9
    return cost





