#-*- coding: utf-8 -*-
print("Hello world!")
import csv
import os
import copy as c

print("Hello world!")
country_names = ['그리스','네덜란드','노르웨이','뉴질랜드','덴마크','독일','라트비아','러시아','룩셈부르크','리투아니아','멕시코','미국','벨기에','스웨덴','스위스','스페인','슬로바키아','슬로베니아','아이슬란드','아일랜드','에스토니아','영국','오스트레일리아','오스트리아','이스라엘','이탈리아','일본','체코','칠레','캐나다','콜롬비아','터키','포르투갈','폴란드','프랑스','핀란드','한국','헝가리']
genders = ["남자",'여자','개인 전체']

table = []
temp = []

def get_ans_yes_or_no_or_another() :
    while True :
        ans = input("입력 : ")
        
        if ans == "dd" or ans == "d" or ans == "y" or ans == "ㅛ" or ans == "1" or ans == "yes" or ans == "YES" or ans == "DD" or ans == "D" or ans == "Y" or ans == '응' or ans == '어' or ans == '네' or ans == '예':
            return 1
        elif ans == 's' or ans == 'ss'  or ans == 'SS' or ans == 'S' or ans == 'NO' or ans == 'no' or ans == 'n' or ans == 'N' or ans == '0'  or ans == '아니'  or ans == 'ㄴㄴ' or ans == 'ㄴ' or ans == '아니오' or ans == '아니요':
            return 0
        elif ans == "both" or ans == "BOTH" or ans == "둘다" or ans == "총계" or ans == "총합" or ans == "전부" or ans == "2":
            return 2
        else :
            continue

def get_ans_kinds_of_country() :
    global country_names
    temp_ans = []
    while True :
        print("사용가능한 국가는 다음과 같습니다.(고르기 종료 : exit입력)")
        show_all_country_names()
        if len(temp_ans)!=0 :
            print("지금까지 고른 국가 :",end=" ")
            for i in range(0,len(temp_ans)) :
                print("{}".format(temp_ans[i]),end=" ")
        temp_ans_country_name = input("입력 : ")
        if temp_ans_country_name == "종료" or temp_ans_country_name == "exit" :
            if len(temp_ans) < 2 :
                print("적어도 두개를 고르셔야합니다.")
                continue
            else :
                break
        if temp_ans_country_name in country_names :
            temp_ans.append(temp_ans_country_name)
        else :
            continue
    return temp_ans



def get_real_length_on_CMD(string) :
    count = 0
    for i in range(len(string)) :
        if string[i].encode().isdigit() :
            count += 1
        else :
            if string[i].encode().isalpha():
                #영어 맞음
                count += 1
            else :
                count += 2 
    return count

def check_country_section(country_name) :
    #나라 이름 받고서 country_names에 해당하는 위치(상수)를 반환함.
    global country_names
    #print("country_name :",country_name)
    for i in range(len(country_names)) :
        if str(country_name) == str(country_names[i]) :
            a = c.deepcopy(i)
            #print("a :",a)
            #print("i :",i)
            return a
def check_gender_section(gender_name) :
    global gendgers
    for i in range(genders) :
        if str(gender_name) == str(genders[i]) :
            a = c.deepcopy(i)
            return a

def setting_table_level_1() :
    #1단계, 테이블 불러오기  
    global table
    with open('table2.csv','r') as f :
        reader = csv.DictReader(f)
        for row in reader :
            table.append(row)
            #print(row)      

def setting_table_level_2() :
    #2단계, 각 나라 위치에 맞는 곳에 국가 데이터 append 하기
    global temp
    
def show_all_country_names() :
    for i in range(0,len(country_names)//5) :
        for j in range(0,5) :
            print(country_names[i*5+j],end="\t")
            if len(country_names[i*5+j]) < 4 :
                print("\t",end="")
        print("")
    for i in range(0,len(country_names)%5) :
        print(country_names[-i],end="\t")
        if len(country_names[-i]) < 4 :
            print("\t",end="")

def show_all_country_ops(country_name) :
    global table
    fir = 1
    print("국가 : {}".format(country_name))
    for i in range(len(table)) :
        
        if table[i]['1'] == country_name :
            if fir == 1 :
                a = table[i]['2']
                print("성별 : {}".format(table[i]['2']))
                print("\t나이\t\t\t고용인구비율\t노동참여비율\t실업률")
                fir = 0
            if a != table[i]['2'] :
                a = table[i]['2']
                print("성별 : {}".format(table[i]['2']))
                print("\t나이\t\t\t고용인구비율\t노동참여비율\t실업률")
            a = table[i]['2']

            if get_real_length_on_CMD(table[i]['3']) > 8 :
                print("\t{0}\t".format(table[i]['3']),end="")
            else :
                print("\t{0}\t\t".format(table[i]['3']),end="")
            print("\t{0:.2f}\t\t{1:.2f}\t\t{2:.2f}".format(float(table[i]['4']),float(table[i]['5']),float(table[i]['6'])))
            '''
            print("\t연령 : {}".format(table[i]['3']))
            print("\t\t고용인구비율 : {}".format(table[i]['4']))
            print("\t\t노동참여비율 : {}".format(table[i]['5']))
            print("\t\t실업률 : {}".format(table[i]['6']))
            '''

def show_country_ops_center() :
    #나라 정보 출력 기능
    global country_names
    print("출력 가능 국가는 다음과 같습니다.")
    show_all_country_names()
    ans1_country = ""
    while True :
        ans1_country = input("\n국가입력 : ")
        if ans1_country in country_names :
            break
        else :
            print("해당 국가는 포함되지 않았습니다.")
    show_all_country_ops(ans1_country)
        
def show_Unemployment_Rate_center() :
    #나라별 실업률 정보 출력 기능 센터
    global country_names


    kind_of_age = []
    kind_of_country = []
    kind_of_gender = []
    #!여기 부분 종류 고르는 것들 구조화 시켜서 더 다양하게 고를 수 있게 하기
    print("모든 국가의 실업률 정보를 출력하시겠습니까? (Y/N)")
    ans1_ur_c = get_ans_yes_or_no_or_another()
    if ans1_ur_c == 1 :
        kind_of_country = c.deepcopy(country_names)
    else :
        kind_of_country = get_ans_kinds_of_country()


    print("모든 나이의 실업률 정보를 출력하시겠습니까? 아니면\n실업률 총계만 출력하시겠습니까?\n모든 나이 = Y / 총계만 = N")
    ans2_ur_c = get_ans_yes_or_no_or_another()
    if ans2_ur_c == 0 :
        kind_of_age = ['총계']
    else :
        kind_of_age = ['15~19세','20~24세','25~29세','30~34세','35~39세','40~44세','45~49세','50~54세','55~59세','60~64세','65세 이상']
    

    print("모든 성별의 실업률 정보를 출력하시겠습니까? 아니면\n남자만의 실업률 정보를 출력하시겠습니까? 아니면\n여자만의 실업률 정보를 출력하시겠습니까?\n개인 전체 = 2 / 남자 = 1 / 여자 = 0")
    ans3_ur_c = get_ans_yes_or_no_or_another()
    if ans3_ur_c ==  0:
        kind_of_gender.append('여자')
    elif ans3_ur_c ==  1:
        kind_of_gender.append('남자')
    elif ans3_ur_c ==  2:
        kind_of_gender.append('개인 전체')

    show_Unemployment_Rate(kind_of_country,kind_of_gender,kind_of_age)

def show_Unemployment_Rate(country,gender,age) :
    global table
    '''
    이건 각 나라의 성별, 나이에 따라 실업률을 출력할 수 있습니다.
    S(how)U(nemployment)R(ate)에서는 country, gender, age 모두 배열로써 받습니다.
    
    '''
    print("country :",country)
    print("gender :",gender)
    print("age :",age)
    print("1")
    for i in range(len(table)) :
        #print("i :",i)
        #print("table[i]['1'] == country :",table[i]['1'] == country)
        for e in range(len(country)) :
            if table[i]['1'] == country[e] :
                fir_country = 1
                #print("국가 : {}".format(country[e]))
                for j in range(len(gender)) :
                    fir_gender = 1
                    if table[i]['2'] == gender[j] :
                        for k in range(len(age)) :
                            if table[i]['3'] == age[k] :
                                if fir_country == 1 :
                                    print("국가 : {}".format(country[e]))
                                if fir_gender == 1 :
                                    print("성별 : {}".format(gender[j]))
                                    fir_gender = 0
                                print("나이 : {} / 실업률 : {}".format(age[k],table[i]['6']))



            
            


    

        
    
    
    
    
 

print("Hello world!")
setting_table_level_1()
'''
a = str(table)
for i in range(len(a)) :
    print(a[i],end='')
    if a[i] == "}" :
        print("")
'''
show_all_country_ops("한국")
while True :
    print("OECD 가입국가의 LFS입니다.")
    print("1.국가의 모든 LFS 정보 출력")
    print("2.실업률 정보 출력")
    ans_main_1 = input("종류선택 : ")
    if ans_main_1 == '1' :
        show_country_ops_center()
    elif ans_main_1 == '2' :
        show_Unemployment_Rate_center()
    else :
        continue