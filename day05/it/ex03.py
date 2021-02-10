'''
and 연산자는 1개라도 (거짓)이 존재하면 결과는 false
True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False

or 연산자는 1개라도 True(참)이 존재하면 결과는 True
True and True   -> True
True and False  -> True
False and True  -> True
False and False -> False


not 연산자는 1개의 피연산자를 가지게 되며, 결과를 반전시킴
True -> False
False -> True

'''

print("False or False : ", False or False)
print("True or False : ", True or False)
print("False or True : ", False or True)
print("True or True : ")
print()
print("not(False or False) : ", not(False or False))
print("not(True or True) : ", not(True or True))
print()


print("False and False : ", False and False)
print("True and False : ", True and False)
print("False and True : ", False and True)
print("True and True : ")
print()
print("not(False and False) : ", not(False and False))
print("not(True and True) : ", not(True and True))
print()




