v1 = 1
res = type(v1) is int

print("type(v1) =",type(v1))
print("res = {}".format(res))

result = type(v1) is not int
print('res = {}'.format(res))

print()
v2 = '1'
res = type(v2) is int
print("type(v2) =",type(v2))
print("res = {}".format(res))

res = type(v2) is not int
print("res = {}".format(res))

