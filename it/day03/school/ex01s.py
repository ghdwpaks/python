print('성별 : %s, 연령 : %d 세' % ('남자',27))
print('성별 : {0}, 연령 : {1} 세'.format('남자',27))

print("오늘 소개할 작품은 %s의 %d년 작품 %s입니다."%('고흐',1889,'자화상'))
print()

print("물건이 %d개 있어요." % (1))
print("물건이 %d개 있어요." % (10))
print("물건이 %d개 있어요." % (100))
print()

print("물건이 %3d개 있어요." % (1))
print("물건이 %3d개 있어요." % (10))
print("물건이 %3d개 있어요." % (100))
print()

print("물건이 %4d개 있어요." % (1))
print("물건이 %5d개 있어요." % (10))
print("물건이 %6d개 있어요." % (100))
print()

print("원주율은 %f입니다." % (3.141592))
print("원주율은 %.2f입니다." % (3.141592))
print("원주율은 %5.2f입니다." % (3.141592))
print()

print("성별{0:1},연령:{1:4d}세".format("남자",27))
print("성별{0:1},연령:{1:10d}세".format("남자",27))
print("성별{0:1},연령:{1:10}세".format("남자",27))
print("성별{0:1},연령:{1:15f}세".format("남자",27))
print()

print("내 이름은".ljust(10),"ghdwpaks")
print()

v1 = True
print(int(v1))
v2 = 5
v3 = 2.5
v4 = "파이썬"

print(v1,"\n",v2,"\n",v3,"\n",v4)
print()
print()

arr=[]
arr=[1,2,3,4,5,6,7,8,9]
print(arr[4])
print(arr[2:6]) #print(arr[시작할 객체의 위치 : 끝날 객체의 위치]) //다만, '시작할 객체의 위치'의 내용물은 포함하지 않는다
print(arr[2:4])
print(arr[-3:-1])
print()

#print(arr[0:9:2])#홀수만 출력함
#홀수만 출력함
'''
for arr in arr:
    if arr % 2 == 1 :
        print(arr)
print()
'''
#tlqkf 이거 위에 arr[0:9:2]부분이랑 for문 부분 주석처리 하니까 뒤에 있는것들 정상작동하는데
#for문에 뭔짓을 하는거길래 이렇게 되는건지 모르겠음

arr2=[]
arr2=[arr,[10,11,12,13,14,15,16,17,18,19,20,21]]
print("leng of arr2 :",len(arr2))
print("leng of arr2[0] :",len(arr2[0]))
print("leng of arr2[1] :",len(arr2[1]))
print()

print("arr print start")
for i in arr : print(i)
print("arr print finished")
print()

print("arr2 print start")
for i in arr2 : print(i)
print("arr2 print finished")
print()


#print(arr[0:9:2])#홀수만 출력함
#v2arr = [[arr],[10,11,12,13,14,15,16,17]]
#print(v2arr)

dict2 = {}
dict2 = {"m":17,"y":43}
print(dict2["m"])
print(dict2["y"])
print()


dict1 = {}
dict1 = {
    "first":{"mouse":3,"penguin":5},
    "sec":{"mouse":6,"penguin":7}
}
print(dict1["first"]["mouse"])
print(dict1["first"]["penguin"])
print(dict1["sec"]["mouse"])
print(dict1["sec"]["penguin"])
print()

V = 15.364
W = 15
X = True
Y = 2+3j
Z = "파이썬이란?"
print("V: type", type(V))
print("W: type", type(W))
print("X: type", type(X))
print("Y: type", type(Y))
print("Z: type", type(Z))

u1 = input("당신의 이름은?\n>>")
print("이름은",u1,"입니다.")

a1 = 57 ; b1 = 25 ; c1 = 10.5
print("a1+b1 :",a1+b1)
print("c1-a1 :",c1-a1)
print("")
print(a1)
print(a1)