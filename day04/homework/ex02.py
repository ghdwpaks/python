print("Hello world!")

name = input("당신의 이름은?\n>>")
c = int(input("{}님의 C 언어 점수는 몇점입니까?\n>>".format(name)))
java = int(input("{}님의 Java 언어 점수는 몇점입니까?\n>>".format(name)))
py = int(input("{}님의 python 언어 점수는 몇점입니까?\n>>".format(name)))
sum_all = c + java + py
arge = sum_all / 3

print("당신의 프로그래밍 점수 합산은 {}점이며,".format(sum_all))
print("평균점수는 {:.2f}점 입니다.".format(arge))

