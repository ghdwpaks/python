print("Hello world!")

userans1 = input("당신의 주민번호 앞자리는 무엇입니까?")

usernum1 = userans1[0:2]
usernum2 = userans1[2:4]
usernum3 = userans1[4:6]
if  int(usernum1) > 50  :
    year = 19
else :
    year = 20
#print(usernum1,usernum2,usernum3)

print("당신의 생일은 {}{}년 {}월 {}일 입니다!".format(year,usernum1,usernum2,usernum3))

