dict_data = {'key01': 1,'key02': 2,'key03': 3,'key04': 4}

print("dict_data.get('key01') :",dict_data.get('key01'))
print("dict_data.get('key02') :",dict_data.get('key02'))
print("dict_data.get('key03') :",dict_data.get('key03'))
print("dict_data.get('key04') :",dict_data.get('key04'))

find_key = input("검색 키 입력 :")
if dict_data.get(find_key) == None :
    print("검색 테이터가 없습니다.")
else :
    print(dict_data.get(find_key))
