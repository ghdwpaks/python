print("Hello world!")

wp = {  "ar" : {"dm" : 90 , "rpm" : 300} ,
        "smg": {"dm" : 30, "rpm" : 1200} ,
        "hg" : {"dm" : 15, "rpm" : 150}
    }
'''
in2 = input()
print("wp[{}][dm] : {}".format(in2,wp[in2]["dm"]))


print(wp["ar"]["dm"])
print(wp["ar"]["rpm"])

print(wp["smg"]["dm"])
print(wp["smg"]["rpm"])

print(wp["hg"]["dm"])
print(wp["hg"]["rpm"])
'''


print("\n\n\n")
#print("GTA5 에서 어떤 무기를 사용하실건가요?")

while(True) :
    in1 = input("GTA5 에서 어떤 무기를 사용하실건가요?\n>>")
    if in1 == "exit" :
        break
    elif in1 == "kind" :
        print("소총 : AR\n기관단총 : SMG\n권총 : HG")
    elif in1 == "AR" or in1 == "ar" or in1 == "소총":
        in1 = "ar"
        print1 = "소총"
        print("{}의 데미지 : {} , 연사속도 : {}".format(print1, wp[in1]["dm"],wp[in1]["rpm"]))
    elif in1 == "SMG" or in1 == "smg" or in1 == "기관단총":
        in1 = "smg"
        print1 = "기관단총"
        print("{}의 데미지 : {} , 연사속도 : {}".format(print1, wp[in1]["dm"],wp[in1]["rpm"]))
    elif in1 == "HG" or in1 == "hg" or in1 == "권총":
        in1 = "hg"
        print1 = "권총"
        print("{}의 데미지 : {} , 연사속도 : {}".format(print1, wp[in1]["dm"],wp[in1]["rpm"]))
    print("\n\n")
    


print("프로그램을 종료합니다")
    
