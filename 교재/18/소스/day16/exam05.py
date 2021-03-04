url = {}
url['파이썬'] = 'www.python.org'
url['네이버'] = 'www.naver.com'
url['구글'] = 'www.google.com'

print('파이썬 : ', url['파이썬'])
print('구글 : ', url['구글'])
print('네이버 : ', url['네이버'])

data = input('사이트 이름 : ')
print('{} : {}'.format(data, url[data]))
