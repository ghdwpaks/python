data1 = 1
result = type(data1) is int

print("type({}) is int : {}".format(data1, result))

data1 = '1'
result = type(data1) is int
print("type({}) is int : {}".format(data1, result))

result = type(data1) is not int
print('type({}) is not int: {}'.format(data1, result))