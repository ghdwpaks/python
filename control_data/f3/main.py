print("Hello world!")
import csv
import os
import copy as c

print("Hello world!")
temp = [] #temp, 임시 테이블
country_names = ['그리스','네덜란드','노르웨이','뉴질랜드','덴마크','독일','라트비아','러시아','룩셈부르크','리투아니아','멕시코','미국','벨기에','스웨덴','스위스','스페인','슬로바키아','아이슬란드','아일랜드','에스토니아','영국','오스트레일리아','오스트리 아','이스라엘','이탈리아','일본','체코','칠레','캐나다','콜롬비아','터키','포르투갈','폴란드','프랑스','핀란드','한국','헝가리']
def remove_zero(string) :
    for i in range(len(string)) :
        if string[i] == '0' :
            del string[i]
    return string
def check_country_section(country_name) :
    global country_names
    #print(country_name)
    #print(country_names)
    for i in range(len(country_names)) :
        if str(country_name) == str(country_names[i]) :
            print(i)
            
            return i
country = [] #전체 중 나라 구분
for i in range(len(country_names)) :
    country.append([])
#print(country)
gendger = [] #gender, 나라 중 성별구분
age = [] #age, 성별 중 나이 구분
#c <- g <- a
with open('table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        temp.append(row)
        #print(row)
#print(temp[i]["국가"])
for i in range(0,len(temp)) :
    for j in range(0,len(country_names)) :
        if country_names[j] == temp[j]["국가"] :
            country[j].append(check_country_section(temp[i]["국가"]))
            a = check_country_section(temp[j]["국가"])
            #print(a)
#print()




print("Hello world!")
