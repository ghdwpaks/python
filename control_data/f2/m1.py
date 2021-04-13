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
targetc = 0 #도시 타겟 지정
city = "" #도시이름
sexc = '' #성별
def setting_city() :
    global city_name,targetc
    #print("enter1")
    print("\n\n\n")
    
    if targetc == 1:
        city_name = "서울특별시"
    elif targetc == 2:
        city_name = "부산광역시"
    elif targetc == 3:
        city_name = "대구광역시"
    elif targetc == 4:
        city_name = "인천광역시"
    elif targetc == 5:
        city_name = "광주광역시"
    elif targetc == 6:
        city_name = "대전광역시"
    elif targetc == 7:
        city_name = "울산광역시"
    elif targetc == 8:
        city_name = "세종특별자치시"
    elif targetc == 9:
        city_name = "경기도"
    elif targetc == 10:
        city_name = "강원도"
    elif targetc == 11:
        city_name = "충청북도"
    elif targetc == 12:
        city_name = "충청남도"
    elif targetc == 13:
        city_name = "전라북도"
    elif targetc == 14:
        city_name = "전라남도"
    elif targetc == 15:
        city_name = "경상북도"
    elif targetc == 16:
        city_name = "경상남도"
    elif targetc == 17:
        city_name = "제주특별자치도"
    elif targetc == 18:
        city_name = "전역"
    #print("city name =",city_name)


def setting_sexc() :
    print("\n\n\n")
    global sexc
    while True :
        print("1.모두")
        print("2.남자")
        print("3.여자")
        u3 = input("종류선택 : ")
        if u3 == '1' :
            sexc = "계"
            break
        elif u3 == '2' :
            sexc = '남자'
            break
        elif u3 == '3' :
            sexc == '여자'
            break
        else :
            continue
    #print("sexc =",sexc)
def show_ops() :
    global city_name,sexc
    print("\n\n\n")
    for i in range(len(t)) :
        if t[i]['1'] == city_name and t[i]['2'] == sexc:
            #print("결과물 : ",t[i])
            print("행정구역 :\t\t",t[i]['1'])
            if t[i]['2'] == '계' :
                print("성별 :\t\t\t 남녀합산")
            else :
                print("성별 :\t",t[i]['2'])
            print("15세 이상인구(천명):\t",t[i]['3'])
            print("경제활동인구(천명):\t",t[i]['4'])
            print("취업자(천명):\t\t",t[i]['5'])
            print("실업자(천명):\t\t",t[i]['6'])
            print("비경제활동인구(천명):\t",t[i]['7'])
            print("경제활동참가율(%):\t",t[i]['8'])
            print("고용률(%):\t\t",t[i]['9'])
            print("실업률(%):\t\t",t[i]['10'])
def choose_city() :
    global targetc
    p = True
    while p :
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
        print("0.뒤로가기")
        u2 = input("종류선택 : ")
        if "exit" == u2 or "종료" == u2 or '0' == u2 or "EXIT" in u2:
            p = False
        elif int(u2) < 18 and int(u2) > 0 :
            targetc = int(u2)
            p = False
        else :
            continue
def choose_func(input1) :
    if input1 == '1' :
        choose_city()
        setting_city()
        setting_sexc()
        show_ops()
    elif input1 == '2' :
        pass



p = True
while p :
    #os.system("cls")
    print("\n\n\n")
    print("1.도시별 데이터 출력")
    print("2.데이터별 도시 순위")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    elif int(u) < 3 and int(u) > 0 :
        choose_func(u)
    else :
        continue