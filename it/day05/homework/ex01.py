print("Hello world!")

print("당신의 평균 성적은 몇입니까?\n>>" , end="")
score = int(input())
result = score > 60

if result :
    print("합격했습니다!")
else :
    print("탈락했습니다.")

