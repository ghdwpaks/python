'''
csv에는 주석처리 기능이 없기 때문에 여기에다가 데이터를 적음
mdf     마드라조 파일
teq     신시미토 테킬라
ruby    루비 목걸이
bond    무기명 채권
pd      핑크 다이아몬드
pan     팬서 조각상
'''
import csv
import os
a = []
with open('cost_table.csv', 'r') as f :
    reader = csv.DictReader(f)
    #print("reader: " , reader)
    for row in reader :
        #print("row :",row)
        a.append(row)
        #print("a :",a)
#print("a[mdf] =", a[0]["mdf"])

    def print_ops(o,n) :
        print("\n\n")
        print(n)
        print("일반난이도 수입금 : {}".format(a[0][o]))
        print("하드난이도 수입금 : {}".format(a[1][o]))
        print("\n\n")
        os.system('pause')
print("Hello world!")
p = True #pass 이탈 여부
o = "" #object 
while p :
    os.system('cls')
    print("이번 목표물은 무엇인가요?")
    print("1.마드라조 파일")
    print("2.신시미토 테킬라")
    print("3.루비 목걸이")
    print("4.무기명 채권")
    print("5.핑크 다이아몬드")
    print("6.팬서 조각상")
    print()
    print("0.EXIT 종료")

    u = input("목표물 : ")
    if "마드라조" in u or '1' in u or '파일' in u:
        o = "mdf"
        n = "마드라조 파일"
        print_ops(o,n)
    elif "신시미토" in u or '2' in u or '테킬라' in u or '데킬라' in u or '데낄라' in u :
        o = 'teq'
        n = "신시미토 테킬라"
        print_ops(o,n)
    elif "루비" in u or '3' in u or '목걸이' in u:
        o = 'ruby'
        n = "루비 목걸이"
        print_ops(o,n)
    elif "무기명" in u or '4' in u or "채권" in u :
        o = 'bond'
        n = "무기명 채권"
        print_ops(o,n)
    elif "핑크" in u or '5' in u or "다이아" in u or "다이아몬드" in u or "핑다" in u:
        o = 'pd'
        n = "핑크 다이아몬드"
        print_ops(o,n)
    elif "팬서" in u or '6' in u or "펜서" in u or "조각상" in u :
        o = 'pan'
        n = "팬서 "
        print_ops(o,n)
    elif "exit" == u or "종료" == u or '0' == u or "EXIT":
        p = False

    







