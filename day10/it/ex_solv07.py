'''
수를 입력 받아 소수인지 아닌지 판별해서 출력하세요.
소수 : 2,3,5,7,11,13
'''

in1 = int(input("정수 입력 : "))
res = ""
p = [2,3,5,7,11,13]
for i in range(0,len(p)) :
    #print("i =",i)
    #print("p[{}] = {}".format(i,p[i]))
    if in1 % p[i] == 0 :
        #소수가 아니라면
        res = "아닙니다."
        #print("y")
        break
    else :
        res = "맞습니다."

print("{}은 소수가 {}".format(in1,res))

'''선생님 답안'''
data = int(input("입력 : "))
print_string = "소수입니다."
for i in range(2,data) :
    if data % i == 0 :
        print_string = "소수가 아닙니다."

print("{}(은)는 {}".format(data,print_string))





