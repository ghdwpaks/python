import random 

i = 1
while i <= 5 :
    print("{}번째 랜덤 : {}".format(i, int(random.random()* 45) + 1))
    i += 1

for i in range(6,11) :
    print("{}번째 랜덤 : {}".format(i,random.randrange(1,46)))

