'''
세 개의 수를 입력 받아서 큰 수를 출력하시오
'''
arr = [1,2,3]
for i in (0 , 3) :
    arr[i] = int(input("{}번째 수 입력 : ".format(i)))
arr.sort()

print("가장 큰 수는 {}입니다.".format(arr[2]))



'''선생님 풀이'''
data1,data2,data3 = input("세 수 입력 : ").split()

data1 = int(data1)
data2 = int(data2)
data3 = int(data3)
max_data = data1
if max_data < data2 :
    max_data = data2
if max_data < data3 :
    max_data = data3
print("{},{},{} 세 수 중 큰 수는 {}입니다.".format(data1,data2,data3,max_data))










