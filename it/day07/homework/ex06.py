l = [0,1,2,3,4,5,6,7,8,9]
s = int(input("정수 입력 : "))


print("{}는 \n{}\n안에 ".format(s,l),end="")
if s in l :
    print("있습니다.")
else :
    print("없습니다.")