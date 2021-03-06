print("Hello world!")

print("이 파일은 기존 vscode와는 다르게 pycharm으로 코딩됐습니다.")

u1 = int(input("정수 입력 : "))

def print_n (d,n) :
    print("{}는 {}의 자리 정수입니다!".format(d,n))


if u1 < 10 :
    print_n(u1,1)
elif u1 < 100 :
    print_n(u1,10)
elif u1 < 1000 :
    print_n(u1,100)