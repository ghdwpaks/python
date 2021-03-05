# number 인자를 사용하는 inc(number), dec(number) 함수를 
# 만들어 함수로 전달한 number 값에 대해 inc 함수는 +1 증가, 
# dec함수는 -1 감소한 값을 반환하게 하시오.
import random

def inc(number) :
    return number + 1

def dec(number) :
    return number - 1

print(inc(10))
print(dec(10))

# start, end 인자를 사용하는 rangeRand(start, end) 함수를 만들고
# start ~ end 까지 랜덤 값을 반환 하도록 하시오.

def rangeRand(start, end) :
    return start + int(random.random() * (end - start + 1))

print()
for i in range(10) :
    print(rangeRand(1, 3))