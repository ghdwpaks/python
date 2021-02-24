
# 다중(중첩) 반복문

i = 0
count = 0
while i < 10 :
    j = 0
    while j < 10 :
        count += 1
        j += 1
    i += 1

print('하위 while문의 반복 횟수 : ', count)

count = 0
for i in range(10) :
    for j in range(10) :
        count += 1

print('하위 for문의 반복 횟수 : ', count)