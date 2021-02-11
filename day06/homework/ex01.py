print("Hello world!")


for i in range(0,10) :
    print("{}번째 Hello".format(i))


print("\n\n분기점\n\n")

arr1 = ["ghd","wp","aks"]
print("len(arr1) : {}".format(len(arr1)))

for i in (0 , len(arr1)) :
    print("Hello")
    print("i : {}".format(i))
    #print("arr1[{}] : {}".format(i,arr1[i]))

i = 0
print()
while i < 3 :
    print("i : {}".format(arr1[i])) 
    i += 1

print()
i = 0
print("len(arr1) : {}".format(len(arr1)))
for i in (0, len(arr1)) :
    print("i : {}".format(i))
    print("Hello")

print()
i = 0
for i in arr1 :
    print("i : {}".format(i))

print()



