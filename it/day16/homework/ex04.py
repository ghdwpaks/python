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

for i in range(0,len(d)) :
    print("i :",i)
    #print("",pop())
