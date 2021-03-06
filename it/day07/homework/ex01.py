print("Hello world!")

nm = input("이름 : ")
age = int(input("나이 : "))
res = ""

if age < 7 :
    res = "유치원생"
elif age < 14 :
    res = "초등학생"
elif age < 17 :
    res = "중학생"
elif age < 21 :
    res = "고등학생"
else :
    res = "대학생"

print("{}님은 {}입니다.".format(nm,res))







