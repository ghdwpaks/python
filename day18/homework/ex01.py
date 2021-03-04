print("입력예시) jo 910308-3022023")
u = input("주민등록번호 : ")
u = u.strip()

d1 , d2 = u.split("-")
d1 = d1.strip()

d11, d12 = d1.split(" ")
#print("u.split(" ") : ",u.split(" "))
d2 = d2.strip()

d2 = "*"*(len(d2))

print("{}님의 주민등록번호는 {}-{}입니다.".format(d11,d12,d2))