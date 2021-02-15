dict1 = {"name" : "ghdwpaks", "cost" : 4000}

arr = []
arr.append(1)
print("arr =",arr)


arr.append(2)
print("arr =",arr)

arr.append(dict1)

print("arr =",arr)
print(arr[2])
print(arr[2]["cost"])
dict1 = {"name" : "ghdwpaks22","cost" : 7000}

arr.append(dict1)
print(arr)
print()
print("arr[3]['cost'] : ",arr[3]["cost"])
