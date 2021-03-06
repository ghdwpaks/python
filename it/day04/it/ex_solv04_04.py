name = input("당신의 이름은 무엇입니까? ")
kscore = int(input("{}님의 국어 점수 : ".format(name)))
escore = int(input("{}님의 영어 점수 : ".format(name)))
mscore = int(input("{}님의 수학 점수 : ".format(name)))
sum_all = kscore + escore + mscore

print("======================")
print("이 름 : {}".format(name))
print("======================")
print("국 어 : {}".format(kscore))
print("영 어 : {}".format(escore))
print("수 학 : {}".format(mscore))
print("======================")
print("합 계 : {}".format(sum_all))
print("======================")

'''선생님 풀이'''
print("\n\n분기점\n\n")
name = input('당신의 이름은 무엇입니까? ')
kor = int(input("{}님의 국어 점수 : ".format(name)))
eng = int(input("{}님의 영어 점수 : ".format(name)))
math = int(input("{}님의 수학 점수 : ".format(name)))
sum_data = kor + eng + math

print("="*15)
print("이름 : {}".format(name))
print("="*15)
print("국어 : {}".format(kor))
print("영어 : {}".format(eng))
print("수학 : {}".format(math))
print("="*15)
print("합계 : {}".format(sum_data))
print("="*15)