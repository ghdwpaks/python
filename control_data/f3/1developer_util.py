s = """
그리스
네덜란드
노르웨이
뉴질랜드
덴마크
독일
라트비아
러시아
룩셈부르크
리투아니아
멕시코
미국
벨기에
스웨덴
스위스
스페인
슬로바키아
슬로베니아
아이슬란드
아일랜드
에스토니아
영국
오스트레일리아
오스트리아
이스라엘
이탈리아
일본
체코
칠레
캐나다
콜롬비아
터키
포르투갈
폴란드
프랑스
핀란드
한국
헝가리"""
s = s.strip()
s = s.split("\n")
for i in range(0,len(s)) :
    print("'"+s[i]+"'",end="")
    print(",",end="")

country = ['그리스','네덜란드','노르웨이','뉴질랜드','덴마크','독일','라트비아','러시아','룩셈부르크','리투아니아','멕시코','미국','벨기에','스웨덴','스위스','스페인','슬로바키아','아이슬란드','아일랜드','에스토니아','영국','오스트레일리아','오스트리 아','이스라엘','이탈리아','일본','체코','칠레','캐나다','콜롬비아','터키','포르투갈','폴란드','프랑스','핀란드','한국','헝가리']
print("\n\n\n")
for i in range(0,len(country)) :
    if country[i] == '한국' :
        print("i :",i)
kn = "한국(남한)"
if str(kn) == "한국(남한)" :
    print("남한이 맞습니다.")
print("\n\n\n")
b = "ghdwpa0k0s0ghdws0a0k0s"
print(len(b))
def remove_zero(string) :
    temp_string = list(string)
    i = 0
    while True :
        i += 1
        if i < len(temp_string):
            if temp_string[i] == '0' :
                del temp_string[i]
        else :
            break
    string = ''.join(temp_string)
    return string
b = remove_zero(b)
print("b =",b)
print(type(b))
print(b[0])

a = """['ghd':wpaks]['ghd':wpaks]['ghd':wpaks]['ghd':wpaks]"""
print(a)
b = print(a)
print(b)
for i in range(len(a)) :
    print(a[i],end='')
    if a[i] == "]" :
        print("")
