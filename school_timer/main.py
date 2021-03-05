from datetime import datetime
import time
import os
import winsound
sn = "BuzzerSoundEffect.WAV" # sound name
def checkans(s="입력 : ") :
    while True :
        in1 = input(s)
        if in1 == None :
            continue
        if in1 == "1" or in1 == "네" or in1 == "예" or in1 == "ㅖ" or in1 == "P" or in1 == "p" or in1 == "응" or in1 == "어" or in1 == "맞아" or in1 == "yes" or in1 == "YES" or in1 == "y" or in1 == "yeah" or in1 == "ㅇ" or in1 == "Y" or in1 == "dd" or in1 == "dmd" or in1 == "akwdk" or in1 == "dj" or in1 == "akwdk" or in1 == "d" :
            return 1
        elif in1 == "0" or in1 == "아니" or in1 == "ㄴ" or in1 == "아님" or in1 == "아니야" or in1 == "아닙니다" or in1 == "n" or in1 == "N" or in1 == "nope" or in1 == "no" or in1 == "NO" or in1 == "ㄴㄴ" or in1 == "아니요" or in1 == "ss" or in1 == "s" or in1 == "dksl" or in1 == "dksldy" :
            return 0

def getclasstime(tmp) :
    class_h , class_m = tmp.split(".")
    class_h = int(class_h)
    class_m = int(class_m)
    class_time_ops = [class_h,class_m]
    return class_time_ops


def checktime(ops) :
    now = datetime.now()
    h = now.hour    #현재 시간
    m = now.minute + 1  #현재 분
    for i in range(0,len(ops[1])) :
        if ops[0][i] == 1 :
            cto = getclasstime(ops[1][i])
            if cto[0] <= h and cto[1] <= m :
                print("지금은 수업중입니다!")
            print("다음수업시작까지 {}시간 {}분 남았습니다.".format(cto[0] - h,cto[1]-m))
            if h == cto[0] :
                if m > cto[1] - 5 :
                    print("소리내기")
                    winsound.PlaySound(sn,winsound.SND_LOOP)
            break






s = "Hello world!"

now = datetime.now()

class_time = ["08.40","09.30","10.20","11.10","12.50","13.40","14.30"]
ans = []
ops = []#옵스 ops 0번째가 사용자 대답, 1번째가 수업시작시간이다.
for i in range(0,7) :
    ans.append(checkans("오늘은 {}교시 수업이 있습니까? >>".format(i+1)))
    
#print(ans)
ops.append(ans)
ops.append(class_time)
#print(ops)
h = now.hour    #현재 시간
m = now.minute  #현재 분
#print("지금은 {}시 {}분 입니다.".format(h,m))


while True :
    os.system("cls")
    h = now.hour    #현재 시간
    m = now.minute  #현재 분
    print("지금은  ",end="")
    for i in range(0,len(ops[0])) :
        if ops[0][i] == 1:
            print(i+1,end="")
            cto = getclasstime(ops[1][i])
            if cto[0] <= h :
                if cto[1] <= m :
                    ops[0][i] = 0
            if i != len(ops[0]) -1 :
                print("  ",end="")
    print(" 교시에 수업이 있습니다.")
    

    checktime(ops)
    time.sleep(0.5)






