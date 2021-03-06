n = input("문장 입력 : ")

print(len(n))
print(n[0])
ni = []
for i in range(0,len(n)) :
    ni.append(int(n[i]))

for i in range(0,len(ni)) :
    print(ni[i],end="")