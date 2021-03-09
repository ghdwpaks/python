def alba(**args):
    print(type(args))
    result = args['day'] * args['time'] * args['won']
    return result

num = int(input('1. 기본급\n2. 일별 계산\n선택 > '))
if num == 1:
    result = alba(day=30, time=8, won=8500)
elif num == 2:
    day = int(input('일한 날짜 입력(몇일) : '))
    result = alba(day=day, time=8, won=8500)

print("급여 : {:,}원 입니다".format(result))