
import random
arr = []
for i in range(0,6) :
    p = True
    tmp = 0
    while p :
        tmp = random.randrange(1,46)
        if tmp in arr :
            p = True
        else :
            p = False
            arr.append(tmp)

for i in arr :
    print(i)


    