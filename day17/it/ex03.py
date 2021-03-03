import copy
list_data1 = [1,2,3]
list_data2 = list_data1 #얕은복사
#얕은복사는, 복제하는객체와 복제당하는 객체가 가리키는 , 실제 데이터가 있는 목적지(주소)가 똑같은 상태로 복사가 되지만
list_data2 = copy.deepcopy(list_data1)#깊은 복사
#깊은 복사는, 복제하는 객체와 복제당하는 객체가 서로 다르게, 실제 데이터가 있는 목적지와는 다른곳에 똑같은 데이터를 생성한다. 진짜 복사라는거다.

print(list_data1)
print(list_data2)

print("=========")
list_data1.clear()

print(list_data1)
print(list_data2)



