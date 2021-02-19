'''
아래와 같이 출력하시오
1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25
26  27  28  29  30


'''
c = 0
for i in range(0, 6) :
    for j in range(1 , 6) :
        print("{}\t".format(c+j),end="")
    print()
    c += 5
print("\n\n분기점\n\n")

'''선생님 답안'''

for i in range(1,31) :
    print("{}\t".format(i), end="")
    if i % 5 == 0 :
        print()

