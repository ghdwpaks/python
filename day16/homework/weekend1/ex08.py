print("pop. 기본적으로 아무것도 쓰지 않으면 마지막에 있는 인덱스(요소)값을 반환한 후에 삭제한다. 이외의 인덱스 번호를 지정할 수도 있다.")
arr1 = [10,20,30,40,50]
arr2 = [10,20,30,40,50]
print('for 진입 전의 arr :',arr1)

for i in range(0,len(arr1)) :
    garbage = arr1.pop()
    print("{}번째 pop의 arr = {}".format(i+1,arr1))
    print("사출된 gar값 :",garbage,"\n")

print("for 사출 후의 arr :",arr1)

print("\n\n\n")
print("arr2 :",arr2)
arr2.pop(2)
print("arr2 :",arr2)


