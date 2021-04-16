a = [1,1,1,1,1,3,3,4,4,4,5]
b = []
for v in a:
    if v not in b:
        b.append(v)
print(b)

a = [1,1,1,1,1,3,3,4,4,4,5]
print(set(a))