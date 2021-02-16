'''
사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고 결과를 출력 할 때 비만도 값 100을 기준으로 100미만이면 저체중, 100 이상 110 미만은 정상, 110 이상 120 미만 과체중, 120 이상 130 미만 비만, 130 이상은 고도비만으로 출력 하시오.

비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
표준 체중 계산 식 : 표준 체중 = (현재 키 - 100) * 0.9

출력 예제 : 홍길동님의 비만도는 112.15%로 과체중입니다.

'''
print("Hello world!")
nm = input("이름 : ")
h = int(input("키 : "))
w = int(input("체중 : "))



obe = w / ((h-100) * 0.9) * 100

print("{}님의 비만도는 {:.2f}로 ".format(nm,obe),end="")

if obe < 100 :
    print("저체중",end="")
elif obe >= 100 and obe < 110 :
    print("정상",end="")
elif obe >= 110 and obe < 120 :
    print("과체중",end="")
elif obe >= 120 and obe < 130 :
    print("비만",end="")
else :
    print("고도비만",end="")
print("입니다.")


print("\n\n\n분기점\n\n\n")
'''선생님 풀이'''
name = input("이름 : ")
height = float(input("키 : "))
weight = float(input("체중 : "))
std_weight = (height - 100) * 0.9
pat = weight / std_weight * 100
result = ''
if pat >= 130 :
    result = "고도비만"
elif pat >= 120 :
    result = "비만"
elif pat >= 110 :
    result = "과체중"
elif pat >= 100 :
    result = "정상체중"
elif pat < 100 :
    result = "저체중"
print("{}님의 비만도는 {:.2f}%로 {}입니다.".format(name,pat,result))




