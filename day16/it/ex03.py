d = {}
d['id'] = "kyes"
d['pw'] = '1234'
print(d)
print("당신의 아이디는 {}이고, 패스워드는 {}입니다.".format(d['id'],d['pw']))

d2 = {}
d2["품번"] = "A222"
d2["품명"] = "Note8"
d2["가격"] = 100000
print("{}, 가격은{:,}입니다.".format(d2['품명'],d2['가격']))
