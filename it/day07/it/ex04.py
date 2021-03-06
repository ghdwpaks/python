list_data = [1,2,3,4,5]

search_data = int(input("검색 정수 입력 : "))

if search_data in list_data :
    print("{}는 {}안에 존재합니다.".format(search_data,list_data))
else :
    print("{}는 {}안에 없습니다.".format(search_data,list_data))


