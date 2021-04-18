h = "  Happy Programming!"
print(len(h))
'''
글자 수 세기 (개)(공백포함)
결과 : 20
해석 :
  Happy Programming!
00000000011111111112
12345678901234567890
'''
print(h.count("p"))
'''
h문자열에서 'p'라는 글자 개수 세기
결과 : 2
해석 :
  Happy Programming!
    pp
'''
print(h.upper())
'''
모든 문자 대문자로 변환
적용후 :
  HAPPY PROGRAMMING!
적용전 :
  Happy Programming!
'''
print(h.lower())
'''
모든 문자 소문자로 변환
적용후 :
  happy programming!
적용전 :
  Happy Programming!
'''
print(h.strip())
'''
문자열 앞뒤 공백 제거
적용후:
Happy Programming!
적용전:
  Happy Programming!
'''
print(h.replace("Happy","Funny"))
'''
Happy라는 곳을 찾아서 Funny로 변환함
적용후:
  Funny Programming!
적용전:
  Happy Programming!
'''
print(h.replace("Hello","Funny"))
'''
Hello라는 곳을 찾아서 Funny로 변환함
적용후:
  Happy Programming!
적용전:
  Happy Programming!
'''
print(h.find("ap"))
'''
h 문자열에서 왼쪽부터 'ap'라는걸 찾아서 그 위치를 알려줌
결과 : 3
해석 :
  H ap
123 45
'''
print(h.rfind("a"))
'''
h 문자열에서 오른쪽부터 'a'라는걸 찾아서 그 위치를 알려줌
2
결과 : 13
해석 : 
  Happy Progra
00000000011111
12345678901234
'''
print(h.find("zoo"))
'''
근데 못찾으면 -1을 반환함
결과 : -1
'''

