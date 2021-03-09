import copy

dict_all = {}
dict_tmp = {}
idx = 1

dict_tmp['name'] = input('이름 : ')
dict_tmp['mobile'] = input('모바일 : ')
dict_tmp['addr'] = input('주소 : ')

#dict_all[idx] = copy.deepcopy(dict_tmp)
dict_all[idx] = dict_tmp
dict_tmp.clear()


idx += 1
dict_tmp['name'] = input('이름 : ')
dict_tmp['mobile'] = input('모바일 : ')
dict_tmp['addr'] = input('주소 : ')

#dict_all[idx] = copy.deepcopy(dict_tmp)
dict_all[idx] = dict_tmp
dict_tmp.clear()

for k, v in dict_all.items() :
    print('{}번 정보'.format(k))
    for k2, v2 in v.items() :
        print('{}, {}'.format(k2, v2))
