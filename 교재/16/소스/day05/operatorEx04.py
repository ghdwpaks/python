# 논리 연산자

'''
and 연산자는 1개라도 Flase(거짓)이 존재하면 결과는 Flase
True and True -> True
True and False -> False
False and True -> False
False and False -> False

or 연산자는 1개라도 True(참)가 존재하면 결과는 True
True or True -> True
True or False -> True
False or True -> True
False or False -> False

not 연산자는 1개의 피연산자로 구성하며, 결과를 반전시킴
not True -> False
not False -> True
'''
print("False or False : ", False or False)
print("True or False : ", True or False)
print("False or True : ", False or True)
print("True or True : ", True or True)
print('')
print("not(False or False) : ", not(False or False))
print("not(True or True) : ", not(True or True))
print('')

print("False and False : ", False and False)
print("True and False : ", True and False)
print("False and True : ", False and True)
print("True and True : ", True and True)
print('')
print("not(False and False) : ", not(False and False))
print("not(True and True) : ", not(True and True))

