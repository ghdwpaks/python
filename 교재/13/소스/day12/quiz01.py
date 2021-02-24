# 1x2 – 2x3 + 3x4 – 4x5 + 5x6 - …와 같은 규칙으로 
# 합계를 구할 때 합이 100이 넘는 마지막 수 2개를 
# 구하는 프로그램을 작성하여라

data = 1
total = 0

while True :
    if data % 2 == 1:
        total += data*(data+1)
    else:
        total -= data*(data+1)
    # print('{} x {} = {}'.format(data, data+1, total))
    if total >= 100:
        break
    data += 1

print("마지막 두 수는 {}와 {}이며, 합계는 {}입니다.".format(data, data+1, total))
