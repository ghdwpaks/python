a = [1,3,4,2,7,6]
a.sort(reverse=True)
print(a)


print("\n\n\n")
a = [1,3,4,2,7,6]
a.sort()
print("[",end="")
for i in range(len(a)) :
    t = len(a) -i -1
    print(a[t],end="")
    if i != len(a)-1 :
        print(",",end="")
print("]")

print("\n\n\n")
a = [1,3,4,2,7,6]
a.sort()
a.reverse()
a

print("\n\n\n")
a = [1, 3, 4, 2, 7, 6]
a.sort()
b=[]
for i in reversed(a):
    b.append(i)
print(b)
