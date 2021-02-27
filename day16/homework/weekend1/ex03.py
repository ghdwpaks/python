arr = [10,20,30,40,50]


for i in range(0,len(arr)) :
    tmp = (i+1) * -1
    print("arr[{}] = {}".format(tmp,arr[tmp]))
print(arr)
print(arr[-8:-1])
#? 배열[음수포함:음수미포함]이렇게 하면 마지막 행은 출력을 못하는데?
print(arr)
print(arr[-7:-1])

