n = input("정수 입력 : ")

ni = int(n)
lenn = len(n)
ns = str(ni)
c = 0 #박수를 치는 횟수

for i in range(0,ni + 1) :
    si = str(i)
    print("i :",i)
    for j in range(0,len(si)) :
        print("si[{}] = {}".format(j,si[j]))
        if si[j] == '3' or (int(si[j]) % 3 == 0 and int(si[j]) > 0):
            print("C++")
            c += 1
    print()
print("c :",c)


