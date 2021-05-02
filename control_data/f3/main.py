#-*- coding: utf-8 -*-
print("Hello world!")
import csv
import os
import copy as c

print("Hello world!")
country_names = ['그리스','네덜란드','노르웨이','뉴질랜드','덴마크','독일','라트비아','러시아','룩셈부르크','리투아니아','멕시코','미국','벨기에','스웨덴','스위스','스페인','슬로바키아','슬로베니아','아이슬란드','아일랜드','에스토니아','영국','오스트레일리아','오스트리아','이스라엘','이탈리아','일본','체코','칠레','캐나다','콜롬비아','터키','포르투갈','폴란드','프랑스','핀란드','한국','헝가리']

temp = [] #temp, 임시 테이블
country = [] #전체 중 나라 구분
gendger = [] #gender, 나라 중 성별구분
age = [] #age, 성별 중 나이 구분
def remove_zero(string) :
    #들어온 변수에 대해서, 0을 제거해주는 변수
    string = str(string).strip()
    print("string :",string)
    temp_string = list(string)
    i = 0
    while True :
        i += 1
        if i < len(temp_string):
            if temp_string[i] == '0' :
                del temp_string[i]
        else :
            break
    string = ''.join(temp_string)
    print(string)
    return int(string)
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

def setting_table_level_1() :
    #1단계, 테이블 불러오기  
    global temp
    with open('table.csv','r') as f :
        reader = csv.DictReader(f)
        for row in reader :
            temp.append(row)
            #print(row)      

def setting_table_level_2() :
    #2단계, 각 나라 위치에 맞는 곳에 국가 데이터 append 하기
    global temp, country
    for i in range(0,len(temp)) :
        #print("i :",i)
        temp_type = ["성별",'연령별','고용/인구 비율','노동참여 비율','실업률']
        temp_for_appending = dict({})
        #print("temp_for_appending :",temp_for_appending)
        for j in range(len(temp_type)) :
            #print("j :",j)
            temp_for_appending[str(temp_type[j])] = temp[i][str(temp_type[j])]
        #print("temp_for_appending :",temp_for_appending)
        country[check_country_section(temp[i]['국가'])].append(temp_for_appending)
        
        #temp[i]['성별'],temp[i]['연령별'],temp[i]['고용/인구 비율'],temp[i]['노동참여 비율'],temp[i]['실업률']

def setting_country_list() :
    global country
    for i in range(len(country_names)) :
        country.append([])


            

print("Hello world!")
a = check_country_section("칠레")
print(a)
setting_country_list()
setting_table_level_1()
print("len(temp) :",len(temp))
#print("1",temp)
setting_table_level_2()
printing = str(country)
for i in range(0,100) :
    print("\n")

for i in range(len(printing)) :
    print(printing[i],end='')
    if printing[i] == "]" or printing[i] == "}" :
        print("")