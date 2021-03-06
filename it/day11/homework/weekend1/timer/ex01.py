import time
import winsound
sn = "BuzzerSoundEffect.WAV" # sound name


def only_number(n,s) :
    n = int(n)
    while(True) :
        print("{} >>".format(s),end='')
        n = input()
        #print(a.isdigit())
        if n.isdigit() :
            n = int(n)
            break
        else :
            print("다시 입력해주세요.")
            continue
    return n

print("Hello world!")

um = 0 #user int input minute
us = 0 #user int input second

um = only_number(um,"분")
us = only_number(us,"초")
t = (((um * 60) + us) * 2)/3 #줌 수업시간 (초)
s = time.time()#Start. s에는 이 명령을 실행한 그 즉시의 시간만을 가진다
print("실제 수업 재생 시간 : {}분 {}초".format(int((t // 60)),int((t % 60))))

p = True
while p :
    n = int(time.time() - s) #실제 경과 시간
    if t < n :
        p = False
print("수업이 끝났습니다!")
winsound.PlaySound(sn,winsound.SND_PURGE)
#input1 = input("")


#print(type(s))
'''
while True :
    print("현재 {}초 경과".format(time.time() - s))
'''




