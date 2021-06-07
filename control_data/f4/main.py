import csv
import os
import copy as c
table = []
with open('table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        table.append(row)
        #print(row)



def setting_product_short_name() :
    global table
    names_product = []
    for i in range(len(table)) :
        if table[i]['1'] not in names_product :
            names_product.append(table[i]['1'])
    #print(names_product)

    names_product2 = []
    for i in range(len(names_product)) :
        names_product2.append(c.deepcopy(names_product[i].split(']')[0]))

    for i in range(len(names_product2)) :
        names_product2[i] = names_product2[i] + ']'

    names_product3 = []
    for i in range(len(names_product2)) :
        if names_product2[i] not in names_product3 :
            #print(names_product2[i])
            names_product3.append(names_product2[i])
    return names_product3
def setting_product_long_name() :
    global table
    names_product = []
    for i in range(len(table)) :
        if table[i]['1'] not in names_product :
            names_product.append(table[i]['1'])
    return names_product

def setting_kinds_of_subjects() :
    #구축중단
    global table
    n = setting_product_long_name()
    print("\n\n\n")
    print("n :",n)
    print("\n\n\n")
    temp = []

    temp_n1 = [] #이름 구분
    temp_n2 = [] #단위 구분
    temp_n3 = [] #등급 구분

    temp_sub_name = n[0] #종목변경인식용 변수
    for i in range(len(table)) :
        for j in range(len(n)) :

            if table[i]['1'] == n[j] :
                if not table[i]['1'] == temp_sub_name :
                    for k in range(len(temp)) :
                        if table[i]['1'] not in names_product :
                            names_product.append(table[i]['1'])
                        if temp_n1 == temp[k]['1'] :
                            if temp_n2 == temp[k]['2'] :
                                if temp_n3 == temp[k]['3'] :
                                    pass

                        temp_n1 = temp[k]['1']
                        temp_n2 = temp[k]['2']
                        temp_n3 = temp[k]['3']



                temp.append(table[i])
                '''
                if table[i]['2'] not in temp_n1 :
                    temp_n1.append(table[i]['2'])
                temp_sub_name = table[i]['1']
                for k in range(len(temp_n1)) :
                '''
                
    for i in range(len(temp_n1)) :
        pass



def integrate_subjects() :
    global table
    names_product = setting_product_long_name()
    temp = []
    temp_keys = []
    for i in range(len(names_product)) :
        for j in range(len(table)) :

            if table[j]['1'] == names_product[i] :
                temp.append(table[j])
                

def print_table_at_str(target_table,keyword) :
    strings = str(target_table)
    for i in range(len(strings)) :
        print(strings[i],end='')
        if strings[i] == keyword :
            print("")

def get_subject_count(sub_name) :
    count = 0 
    for i in range(len(table)) :
        for j in range(1,8) :
            if table[i][str(j)] == sub_name :
                count += 1    
    print(count)
    return count

def get_subjects_name(num) :
    global table
    num = str(num)
    subs = []
    for i in range(len(table)) :
        if table[i][num] not in subs :
            subs.append(table[i][num])
    subs.sort()
    #print(subs)
    return subs

def get_big_subject_name(num,keyword) :
    subs_name = get_subjects_name(num)
    big_subs_names = []
    for i in range(len(subs_name)) :
        target_point = 0
        for j in range(len(subs_name[i])) :
            if subs_name[i][j] == keyword :
                target_point = j
                break
        if not subs_name[i][:(target_point+1)] in big_subs_names :
            big_subs_names.append(subs_name[i][:(target_point+1)])
    return big_subs_names







#1등급을 고른다면, 각 항목에 관한 것들 출력 해주기

lank_1 = get_big_subject_name(1,"]")
#print_table_at_str(lank_1,',')
#print("\n\n",len(lank_1))

while True :
    print("농수산물 정보 출력 시스템에 진입했습니다.")
    print("원하는 기능을 '숫자로만' 선택해주세요.")
    print("1.품목명별 정보 출력")
    print("2.단위별 정보 출력")
    print("3.등급별 정보 출력")
    print("4.가격별 정보 출력")
    print("5.산지별 정보 출력")
    print("6.친환경 구분별 정보 출력")
    select1_subject = input("입력 : ")
    if select1_subject == '1' :
        sector_sub1()
