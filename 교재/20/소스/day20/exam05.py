def func(arg) :
    return arg ** arg

f = func
print(f(2))
print(f(3))
print(f(4))

list_data = [func, 2]
result = list_data[0](list_data[1])
print(result)