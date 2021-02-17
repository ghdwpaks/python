'''
세 수 중 최대/최소 값을 구하는 프로그램 작성
'''

arr = [1,2,3]
for i in (0 , 3) :
    arr[i] = int(input("{}번째 수 입력 : ".format(i)))
arr.sort()

print("가장 큰 수는 {}입니다.".format(arr[2]))
print("가장 작은 수는 {}입니다.".format(arr[0]))


'''선생님 답안'''
data1,data2,data3 = input("세 수 입력 : ").split()
data1 = int(data1)
data2 = int(data2)
data3 = int(data3)
max_data = data1
min_data = data2

if data1 < data2 :
    max_data = data2
    min_data = data1

if max_data < data3 :
    max_data = data3
elif min_data > data3 :
    min_data = data3

print("{},{},{} 수 중에 최댓값{},최솟값 {} 입니다.".format(data1,data2,data3,max_data,min_data))






