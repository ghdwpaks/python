d = int(input("정수 입력 : "))

if d > 999 :
    print("{}는 세자리수 이상입니다.".format(d))
elif d > 99 :
    print("{}는 세자리수입니다.".format(d))
elif d > 9 :
    print("{}는 두자리수입니다.".format(d))
elif d > 0 :
    print("{}는 한자리수입니다.".format(d))
else :
    print("{}는 음수입니다.".format(d))