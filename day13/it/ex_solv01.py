'''
민수는 369게임이 N까지 규칙을 지키며 진행된다면 그때까지의 들은 박수의 횟수가 총 몇번인지 궁금했다. 예를 들어서 N = 14 라면 3,6,9,13에서 각각 한번의 박수를 치게 되므로 총 4회의 박수를 듣게 될 것이다. N = 36이라면 3,6,9,13,16,19,23,26,28,30,32,33,34,35,36에서 박수를 치게 되는데 33,36에서는 두 번 박수츨 쳐야 하므로 총 18회가 된다. 1 이상의 정수 N에 대하여 36게임을 N까지 규칙을 지키며 진행된다면 그댸까지 듣게 되는 박수의 총 횟수를 계산하여 출력하는 프로그램을 작성하시오
'''

n = input("정수 입력 : ")

ni = int(n)
lenn = len(n)
ns = str(ni)
c = 0 #박수를 치는 횟수

for i in range(0,ni + 1) :
    si = str(i)
    #print("i :",i)
    for j in range(0,len(si)) :
        #print("si[{}] = {}".format(j,si[j]))
        if si[j] == '3' or (int(si[j]) % 3 == 0 and int(si[j]) > 0):
            #print("C++")
            c += 1
    #print()
print("총 박수 횟수 :",c)

'''선생님 풀이'''

data = int(input("입력 : "))
for i in range(1,data+1) :
    while True :
        if i == 0 : break
        tmp = i % 10
        j //= 10
        if tmp == 3 or tmp == 6 or tmp == 9 :
            print(i)
            count += 1
print("출력 :",count)




