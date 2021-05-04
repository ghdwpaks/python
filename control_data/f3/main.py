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

def show_country_ops_country(country_name) :
    global table
    for i in range(len(table)) :
        if table[i]['1'] == country_name :
            print("국가 : {}".format(country_name))
            print("\t성별 : {}".format(table[i]['2']))
            print("\t\t연령 : {}".format(table[i]['3']))
            print("\t\t\t고용인구비율 : {}".format(table[i]['4']))
            print("\t\t\t노동참여비율 : {}".format(table[i]['5']))
            print("\t\t\t실업률 : {}".format(table[i]['6']))

def show_country_ops_center() :
    #나라 정보 출력 기능
    global country_names
    print("출력 가능 국가는 다음과 같습니다.")
    show_all_country_names()
    ans1_country = ""
    while True :
        ans1_country = input("\t국가입력 : ")
        if ans1_country in country_names :
            break
        else :
            print("해당 국가는 포함되지 않았습니다.")
    show_country_ops_country(ans1_country)
        
    
    
 

print("Hello world!")
setting_table_level_1()
#show_all_country_names()
while True :
    print("OECD 가입국가의 LFS입니다.")
    print("1.국가의 모든 LFS 정보 출력")
    ans_main_1 = input("종류선택 : ")
    if ans_main_1 == '1' :
        show_country_ops_center()