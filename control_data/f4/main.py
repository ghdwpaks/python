import functions as f



def sector_sub1(table) :

    sub_name = f.gets.get_big_subject_name(table,1,']')
    for i in range(len(sub_name)) :
        if i % 6 == 0 and i != 0:
            print()
        print(sub_name[i],end="\t")
        if f.gets.get_real_length_on_CMD(sub_name[i]) < 8 :
            print("\t\t",end="")
        elif f.gets.get_real_length_on_CMD(sub_name[i]) < 16 :
            print("\t",end="")
    print()
            






#1등급을 고른다면, 각 항목에 관한 것들 출력 해주기
table = f.gets.get_table("table.csv")

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
        sector_sub1(table)
