print("Hello world!")
#요소접근 방식 중에, 음수로 접근 하는 방식이 있다고 함
arr = [10,20,30,40,50]
for i in range(0,len(arr)) :
    print("arr[{}] = {}".format(i,arr[i]))

print("\n\n분기점\n\n")

for i in range(0,len(arr)) :
    tmp = (i+1) * -1
    print("arr[{}] = {}".format(tmp,arr[tmp]))
#근데 한가지 번거로운점은 -1이 양수의 0과 같다는점
