string_data = 'Hello Python'
search_data = input('검색 문자열 입력 : ')

if search_data in string_data :
    print('{}는 {}안에 존재합니다.'.format(search_data, string_data))
else :
    print('{}는 {}안에 없습니다.'.format(search_data, string_data))