'''
수를 입력 받아 0 보다 크고 100보다 작으면
적중범위/비적중범위 구분하여 출력하시오.
'''

in1 = int(input("정수 입력 : "))
if not (in1 > 0 and in1 < 100):
    print("비",end="")
print("적중범위입니다.")