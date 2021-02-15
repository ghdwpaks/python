arr = [1,2,3,4,5]
print("arr의 요소는 ",end="")
for i in arr :
    print(i,end=",")
print("가 있습니다.")

in1 = int(input("숫자입력"))
res = in1 in arr
print("{} in {} : {}".format(in1,arr,res))

res = in1 not in arr
print("{} not in {} : {}".format(in1,arr,res))


v1 = '1'
print("v1 =",v1)
res = v1 in arr
print("{} in {} : {}".format(v1,arr,res))

