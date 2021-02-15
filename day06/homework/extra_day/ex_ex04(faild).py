print("Hello world!")
dict_ = {'name' : "" ,"cost" : ""}
arrs = []
print(dict_)
exit_m = 0
i = 0
while(True) :
    while(True) :
        in1 = input("오늘 구매한 물건의 값은 얼마인가요?\n>>")
        if in1 == "exit" :
            exit_m = 1
            break
        elif in1.isdigit() :
            in1 = int(in1)
            break
        else :
            print("입력이 잘못됐습니다.\n다시 입력해주세요.")
            continue
    if exit_m == 1 :
        break
    in2 = input("오늘 구매한 물건의 이름은 무엇인가요?\n>>")

    #print("dict_ =",dict_)
    dict_ = {'name' : "" ,"cost" : ""}
    dict_["name"] = in2
    dict_["cost"] = in1
    arrs.append(dict_)
    print("\n\n")
    i += 1


sum_all = 0
print("오늘 구매한 물건들의 이름과 가격, 총합은 다음과 같습니다.")
'''
print("arrs[0]['name'] =",arrs[0]['name'])
print("arrs[0]['cost'] =",arrs[0]['cost'])

print("arrs[1]['name'] =",arrs[1]['name'])
print("arrs[1]['cost'] =",arrs[1]['cost'])

print("arrs[2]['name'] =",arrs[2]['name'])
print("arrs[2]['cost'] =",arrs[2]['cost'])
'''
i = 0
while i < len(arrs) :
    #print("i = {}".format(i))
    print("이름 : {} , 가격 : {}".format(arrs[i]["name"],arrs[i]["cost"]))
    sum_all = sum_all + arrs[i]["cost"]
    i += 1



'''
for i in (0, len(arrs)) :
    print("i = {}".format(i))
    print("이름 : {} , 가격 : {}".format(arrs[i]["name"],arrs[i]["cost"]))
    sum_all = sum_all + arrs[i]["cost"]
'''
print("-"*15)
print("총합 : {}원".format(sum_all))
    
    

