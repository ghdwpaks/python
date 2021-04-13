print("Hello world!")
import csv
import os
t = []
with open('table1.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        t.append(row)
        print(row)
print("Hello world!")
print(t)
target = 0 #도시 타겟 지정
city = "" #도시이름
sex = '' #성별
def setting_city() :
    global city_name,target
    print("enter1")
    if target == 1:
        city_name = "서울특별시"
    elif target == 2:
        city_name = "부산광역시"
    elif target == 3:
        city_name = "대구광역시"
    elif target == 4:
        city_name = "인천광역시"
    elif target == 5:
        city_name = "광주광역시"
    elif target == 6:
        city_name = "대전광역시"
    elif target == 7:
        city_name = "울산광역시"
    elif target == 8:
        city_name = "세종특별자치시"
    elif target == 9:
        city_name = "경기도"
    elif target == 10:
        city_name = "강원도"
    elif target == 11:
        city_name = "충청북도"
    elif target == 12:
        city_name = "충청남도"
    elif target == 13:
        city_name = "전라북도"
    elif target == 14:
        city_name = "전라남도"
    elif target == 15:
        city_name = "경상북도"
    elif target == 16:
        city_name = "경상남도"
    elif target == 17:
        city_name = "제주특별자치도"
    elif target == 18:
        city_name = "전역"

def setting_sex() :
    global sex
    while True :
        print("1.모두")
        print("2.남자")
        print("3.여자")
        u3 = input("종류선택 : ")
        if u3 == '1' :
            sex = "계"
        elif u3 == '2' :
            sex = '남자'
        elif u3 == '3' :
            sex == '여자'
        else :
            continue
def show_ops() :
    for i in range(len(t)) :
        if t[i]['1'] == city_name and t[i]['2'] == sex:
            print("Y")
