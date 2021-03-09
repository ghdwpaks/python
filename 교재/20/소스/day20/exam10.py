
def coffee(cnt) :
    '''
        coffee()는 매개변수를 1개 넣어 주셔야합니다.
        매개변수에는 정수의 데이터를 넣어주셔야하며, 양수입니다.
        양수의 데이터는 커피의 수량을 말하며, 가격은 개당 2000원
        10개 초과분에 대해서는 1500원으로 계산된 결과를 
        돌려줍니다.
    '''
    cost = 2000 * cnt
    if cnt > 10 :
        cost = (cnt - 10) * 1500 + 20000
    return cost

def snack(cnt) :
    '''
        snack()는 Argument 1개, 자료형은 양수
        snack() 기능은 개당 1000원에 해당하는 물건의 가격을 구한다.
        snack() 반환 값은 존재하며, 정수이다.
    '''
    cost = 1000 * cnt
    if cnt >= 100 :
        cost = int(cost * 0.88)
    elif cnt >= 10 :
        cost = int(cost * 0.9)
    return cost 


def aaa() :
    pass

def bbb() :
    pass

def ccc() :
    pass