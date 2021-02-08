print("Hello world!")

arr = [0,2,3,4,5,6,7,8,9]
for i in arr : print(i)
print("arr[4] : " , arr[4])

print('\n\n분기점\n\n')

arr2 = [arr,[10,11,12,13,14,15,16,17,18,19]]
for i in arr2 : print(i)
print("arr2[1][4] : ",arr2[1][4])

print('\n\n분기점\n\n')

arr3 = [[20,21,22,23,24,25,26,27,28,29],[arr]]
for i in arr3 : print(i)
print()

arr5 = [arr2,arr3]
for i in arr5 : print(i)
print("arr4[1] :",arr5[1])
print("arr4[1][1] :",arr5[1][1])
print("arr4[1][1][0] :",arr5[1][1][0])
print("arr4[1][1][0][5] :",arr5[1][1][0][5])

