print("Hello world!")

nm = input("이름 : ")
k = input("학교 이름 : ")
res = ""

'''
print("k =",k)
print( "고등학교" in k )
'''

if  '대학'  in k  or '대학교' in k  :
    res = "대학"
elif '고' in k  or '고등학교' in k  :
    res = "고등학교"
elif '중' in k  or  "중학교" in k  :
    res = '중학교'
elif '초' in k  or"초등학교" in k  :
    res = "초등학교"

print("{}님은 {}를 다니는중이십니다.".format(nm,res))





