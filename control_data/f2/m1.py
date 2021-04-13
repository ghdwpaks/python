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
#print(t)
target = 0 #도시 타겟 지정
city = "" #도시이름
sex = '' #성별
def setting_city() :
    global city_name,target
    #print("enter1")
    print("\n\n\n")
    
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
    #print("city name =",city_name)


def setting_sex() :
    print("\n\n\n")
    global sex
    while True :
        print("1.모두")
        print("2.남자")
        print("3.여자")
        u3 = input("종류선택 : ")
        if u3 == '1' :
            sex = "계"
            break
        elif u3 == '2' :
            sex = '남자'
            break
        elif u3 == '3' :
            sex == '여자'
            break
        else :
            continue
    #print("sex =",sex)
def show_ops() :
    print("\n\n\n")
    for i in range(len(t)) :
        if t[i]['1'] == city_name and t[i]['2'] == sex:
            #print("결과물 : ",t[i])
            print("행정구역 :",t[i]['1'])
            print("성별 :",t[i]['2'])
            print("15세 이상인구(천명):",t[i]['3'])
            print("경제활동인구(천명):",t[i]['4'])
            print("취업자(천명):",t[i]['5'])
            print("실업자(천명):",t[i]['6'])
            print("비경제활동인구(천명):",t[i]['7'])
            print("경제활동참가율(%):",t[i]['8'])
            print("고용률(%):",t[i]['9'])
            print("실업률(%):",t[i]['10'])
def choose_func() :
    setting_city()
    setting_sex()
    show_ops()


p = True
while p :
    #os.system("cls")
    print("\n\n\n")
    print("1.서울특별시")
    print("2.부산광역시")
    print("3.대구광역시")
    print("4.인천광역시")
    print("5.광주광역시")
    print("6.대전광역시")
    print("7.울산광역시")
    print("8.세종특별자치시")
    print("9.경기도")
    print("10.강원도")
    print("11.충청북도")
    print("12.충청남도")
    print("13.전라북도")
    print("14.전라남도")
    print("15.경상북도")
    print("16.경상남도")
    print("17.제주특별자치도")
    print("18.전역")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    elif int(u) < 18 and int(u) > 0 :
        target = int(u)
        choose_func()
    else :
        continue