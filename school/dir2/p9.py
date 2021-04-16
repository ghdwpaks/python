#8
import copy as c
a = b = [1,2,3,4,5]

a[1] = 4
print(a)
print(b)
b = a[:]

a[3] = 2
print(a)
print(b)