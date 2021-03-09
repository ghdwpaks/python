# 두 수를 입력받아 큰 수를 반환하는 함수를 만들어주세요.
# 절대 값을 반환하는 함수를 만들어주세요.
# 0~100점의 점수를 입력하면 A~F까지의 학점을 반환하는 함수를 만들어주세요
# 수를 입력하여 소수이다/아니다를 판별하는 함수를 만들어주세요.

def twoMax(data1, data2) :
    if data1 > data2 :
        return data1
    else : 
        return data2

def absolute(data) :
    if data < 0 :
        data = -data
    return data

def grade(data) :
    if data > 100 :
        result = 'F'
    elif data >= 90 :
        result = 'A'
    elif data >= 80 :
        result = 'B'
    elif data >= 70 :
        result = 'C'
    elif data >= 60 : 
        result = 'D'
    else :
        result = 'F'
    return result

def prime(data) :
    cnt = 0
    i = 1
    while i <= data :
        if data % i == 0:
            cnt += 1
        i += 1

    if cnt == 2 :
        return True
    else :
        return False

print(twoMax(11, 2))
print(twoMax(2, 12))

print(absolute(-100))
print(absolute(100))

print(grade(101))
print(grade(100))
print(grade(80))

if prime(10):    print('소수입니다.')
else:  print('소수가 아닙니다.')

if prime(11):    print('소수입니다.')
else:    print('소수가 아닙니다.')
