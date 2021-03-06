'''
주민등록번호 뒷자리 7자리는 모두 '*'로 변경하여 출력 하시오.

'''

ibs = """
jo 910308-3022023
cho 900402-1011232
park 121212-1234567
lee 980908-3121023
kim 900514-2022023
"""
begin = 0
for i in range(ibs.count('-')) :
    begin = ibs.find("-",begin+1)
    ibs = ibs.replace(ibs[begin+1:begin+8],"*******")
    print(ibs)








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


