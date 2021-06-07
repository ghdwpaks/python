import copy as c
import csv
class prints :
    def print_table_at_str(target_table,keyword) :
        strings = str(target_table)
        for i in range(len(strings)) :
            print(strings[i],end='')
            if strings[i] == keyword :
                print("")

class gets :

    
    def get_table(filepath) :
        #table.csv
        table = []
        with open(filepath,'r') as f :
            reader = csv.DictReader(f)
            for row in reader :
                table.append(row)
                #print(row)
        return table


       
    def get_real_length_on_CMD(string) :
        count = 0
        for i in range(len(string)) :
            if string[i].encode().isdigit() :
                count += 1
            else :
                if string[i] == "]" or string[i] == "[" or string[i] == ")" or string[i] == "(" or string[i].encode().isalpha():
                    #영어 맞음
                    count += 1
                else :
                    count += 2 
        #print("GRLOC :",count)
        return count

    
    def get_big_subject_name(table,num,keyword) :
        subs_name = gets.get_subjects_name(table,num)
        big_subs_names = []
        for i in range(len(subs_name)) :
            target_point = 0
            for j in range(len(subs_name[i])) :
                if subs_name[i][j] == keyword :
                    target_point = j
                    break
            if not subs_name[i][:(target_point+1)] in big_subs_names  :
                big_subs_names.append(subs_name[i][:(target_point+1)])
        return big_subs_names

    def get_subjects_name(table, num) :
        num = str(num)
        subs = []
        for i in range(len(table)) :
            if table[i][num] not in subs :
                subs.append(table[i][num])
        subs.sort()
        #print(subs)
        return subs


    def get_subject_count(table, sub_name) :
        count = 0 
        for i in range(len(table)) :
            for j in range(1,8) :
                if table[i][str(j)] == sub_name :
                    count += 1    
        print(count)
        return count

        

    def setting_product_short_name(table) :
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
    
    def setting_product_long_name(table) :
        names_product = []
        for i in range(len(table)) :
            if table[i]['1'] not in names_product :
                names_product.append(table[i]['1'])
        return names_product
    
    
    def integrate_subjects(table) :
        names_product = gets.setting_product_long_name()
        temp = []
        temp_keys = []
        for i in range(len(names_product)) :
            for j in range(len(table)) :

                if table[j]['1'] == names_product[i] :
                    temp.append(table[j])
