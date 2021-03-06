
d = {}
while True :
    k = input("key 값 : ")
    if k == 'exit' :
        break
    v = input("value 값 : ")
    if v == 'exit' :
        break
    t = {k:v}
    d.update(t)
    print(d)

while True :
    u = input("검색할 단어 : ")
    if d.get(u) == None :
        print("검색 결과가 없습니다.")
    else :
        print("결과 :",d.get(u))




