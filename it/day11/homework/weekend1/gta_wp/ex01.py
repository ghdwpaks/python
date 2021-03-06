print("Hello world!")
import csv
import os
wp = []

hg = []
with open('pistol_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        hg.append(row)
wp.append(hg)

ar = []
with open('ar_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        ar.append(row)
wp.append(ar)

sg = []
with open('sg_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        sg.append(row)
wp.append(sg)

smg = []
with open('smg_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        smg.append(row)
wp.append(smg)

dmr = []
with open('dmr_table.csv','r') as f :
    reader = csv.DictReader(f)
    for row in reader :
        dmr.append(row)
wp.append(dmr)

print("Hello world!")
p = True #pass 이탈 여부
o = "" #object 
i = 1
def print_ops(n) :
    print("\n\n")
    i = 1
    pp = True #print_ops pass 
    print("n = ",n)
    print("type(n) = ",type(n))
    print("wp[1][0] : ",wp[n][0])
    print("\n\n")
    while pp :
        #print(wp[n][0])
        print("무기 이름 :{}".format(wp[n][0][str(i)]))
        print("데미지 :\t{}".format(wp[n][1][str(i)]),end='')
        print_ops_graph(wp[n][1][str(i)])
        print("발사 속도 :\t{}".format(wp[n][2][str(i)]),end='')
        print_ops_graph(wp[n][2][str(i)])
        print("명중률 :\t{}".format(wp[n][3][str(i)]),end='')
        print_ops_graph(wp[n][3][str(i)])
        print("범위 :\t\t{}".format(wp[n][4][str(i)]),end='')
        print_ops_graph(wp[n][4][str(i)])
        print("탄창 :\t\t{}".format(wp[n][5][str(i)]),end='')
        print("\n")
        #t = str(i + 1)
        #print("t =",t)
        #print("type(t) = ",type(t))
        #print("wp[n][0][i+1] : ",wp[n][0][str(t)])
        #print("len(wp[n][0]) = ",len(wp[n][0]))
        if i == len(wp[n][0]) :
            break
        i += 1
    print()

def print_ops_graph(n) :
    n = int(n)
    print("\t[",end="")
    if n <= 5 :
        print("#",end="")
    elif n <= 10 :
        print("#"*2,end="")
    elif n <= 15 :
        print("#"*3,end="")
    elif n <=  20:
        print("#"*4,end="")
    elif n <=  25:
        print("#"*5,end="")
    elif n <=  30:
        print("#"*6,end="")
    elif n <=  35:
        print("#"*7,end="")
    elif n <=  40:
        print("#"*8,end="")
    elif n <=  45:
        print("#"*9,end="")
    elif n <=  50:
        print("#"*10,end="")
    elif n <=  55:
        print("#"*11,end="")
    elif n <=  60:
        print("#"*12,end="")
    elif n <=  65:
        print("#"*13,end="")
    elif n <=  70:
        print("#"*14,end="")
    elif n <=  75:
        print("#"*15,end="")
    elif n <=  80:
        print("#"*16,end="")
    elif n <=  85:
        print("#"*17,end="")
    elif n <=  90:
        print("#"*18,end="")
    elif n <=  95:
        print("#"*19,end="")
    elif n <=  100:
        print("#"*20,end="")
    print("]")
    
    


 
while p :
    print("폭발무기와 중화기 또는 mk2무기들은 데이터를 다루지 않습니다.")
    print("1.HG 권총")
    print("2.SMG 기관단총")
    print("3.AR 라이플")
    print("4.SG 샷건")
    print("5.dmr")
    print()
    print("0.EXIT 종료")
    u = input("종류선택 : ")
    if '1' in u or 'HG' in u or "pis" in u or '권총' in u :
        print()
        #print_ops('hg')
        print_ops(0)
    elif '2' in u or 'SMG' in u or "슴지" in u or 'smg' in u:
        print()
        #print_ops('smg')
        print_ops(1)
    elif '3' in u or 'ar' in u or "rifle" in u or '에알' in u or "소총" in u or 'AR' in u:
        print()
        #print_ops('ar')
        print_ops(2)
    elif '4' in u or 'SG' in u or "샷건" in u or 'sg' in u:
        print()
        #print_ops('sg')
        print_ops(3)
    elif '5' in u or 'dmr' in u or "지정사수" in u or '스나' in u:
        print()
        #print_ops('dmr')
        print_ops(4)
    elif "exit" == u or "종료" == u or '0' == u or "EXIT" in u:
        p = False
    else :
        continue



