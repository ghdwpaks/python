d = {}
while True :
    k = input("key 값 : ")
    if k == 'exit' :
        break
    v = input("value 값 : ")
    if v == 'exit' :
        break
    t = {k:v}
    d.update(t)
    print(d)
print(d.keys())
print(d.values())
res1 = 0
for i in range(0,len(d.keys())) :
    res1 += 1
print("res1 =",res1)

print(d.values())
res1 = 0
for i in range(0,len(d.values())) :
    res1 += 1
print("res2 =",res1)

