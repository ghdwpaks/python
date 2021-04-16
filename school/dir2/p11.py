from copy import copy
a=b=[1,2,3,4,5]
a[1]=4
b=copy(a)
print(id(a))
print(id(b))
