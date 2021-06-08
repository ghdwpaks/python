import functions as f



def sector_sub1(table) :

    sub_name = f.gets.get_big_subject_name(table,1,']')
    f.prints.print_strings_dived(sub_name)
    print()
    ans1_big_subs = input("주제 입력 :")
    ans1_big_subs = f.setting.sealing_input_sub(ans1_big_subs)
    subs_ops = f.gets.select_ops_by_keyword(table,ans1_big_subs,1)
    #f.prints.print_table_at_str(subs_ops,'}')
    sub_small_name = f.gets.get_subjects_name(subs_ops,1)

    ans2 = ""
    while True :
        print(ans1_big_subs,"에 적합한 품목은 다음과 같습니다.")
        f.prints.print_strings_dived(sub_small_name)
        print()
        ans2 = input("주제 입력 : ")
        if ans2 in sub_small_name :
            break
        else :
            print("주제를 정확히 입력해주세요.")
    res_ops = f.gets.select_ops_by_keyword(subs_ops,ans2,1)
    #print("res_ops :",res_ops)
    f.prints.print_table_at_str(res_ops,"}")
    
    temp_sub = [res_ops[0]['1'],res_ops[0]['2'],res_ops[0]['3']]
    print()
    print(temp_sub)
    res = []
    cost = 0
    addcost_count = 0
    for i in range(len(res_ops)) :
        canpass = True
        for j in range(len(temp_sub)) :
            if res_ops[i][str(j+1)] == temp_sub[j] :
                cost += int(res_ops[i]['4'])
                addcost_count += 1
            else :
                canpass = False
        if canpass and i != len(res_ops)-1 :
            cost += int(res_ops[i]['4'])
        else :
            res.append([temp_sub[0],temp_sub[1],temp_sub[2],cost//addcost_count])
            temp_sub = [res_ops[i]['1'],res_ops[i]['2'],res_ops[i]['3']]
            cost = 0
            addcost_count = 0
    print(res)
    f.prints.print_table_at_str(res,']')
        
    
    
    
            



 



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
