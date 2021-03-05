
dict_data = {}
dict_data['id'] = 'kyes'
dict_data['pw'] = '1234'

print(dict_data)
print('당신의 아이디는 {}이고, 패스워드는 {}입니다.'.format(dict_data['id'], dict_data['pw']))

dict_data = {'품번' : 'A222', '품명': 'Note8', '가격': 100000}
print(dict_data)
print('{}, 가격은 {:,}원 입니다.'.format(dict_data['품명'], dict_data['가격']))