'''
주민등록번호 뒷자리 7자리는 모두 '*'로 변경하여 출력 하시오.
'''

ids = """
jo 910308-3022023
cho 900402-1011232
park 121212-1234567
lee 980908-3121023
kim 900514-2022023
"""
# print('{}'.format(ids.count('-') ))
#print('{}'.format(ids.find('-', 11)))
begin = 0
for i in range(ids.count('-')) :
    begin = ids.find('-', begin+1)
    ids = ids.replace(ids[begin+1:begin+8], '*******')
    print(ids)

'''
출력 결과
1922년 02월 22일
1990년 04월 02일
2012년 12월 12일
1998년 09월 08일
1990년 05월 14일
'''

infos = """
jo 1922-02-22
cho 1990-04-02
park 2012-12-12
lee 1998-09-08
kim 1990-05-14
"""
# print('{}'.format(infos.count(' ')))
begin = 0
list_data = []
for i in range(infos.count(' ')) :
    begin = infos.find(' ', begin+1)
    list_data.append(infos[begin+1 : begin+11])

#print(list_data)
#['1922-02-22', '1990-04-02', '2012-12-12', '1998-09-08', '1990-05-14'

for i in list_data :
    year, mon, day = i.split('-')
    print('{}년 {}월 {}일'.format(year, mon, day))
