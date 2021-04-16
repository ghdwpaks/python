a= "a:b:c:d"
b = a.split(":")

for i in range(len(b)) :
    print(b[i],end="")
    if i != len(b)-1 :
        print("#",end="")

