a=[],[],[],[],[],[],[]
import csv
with open('passby_data.csv', 'r')as f :
    reader = csv.DictReader(f)
    i=j=0
    for row in reader :
        a[i].append(row)
        j = j+1
        if(j %24 == 0) : #다음 요일로 이동여부를 판단라기 위한 조건문
            i = i+1 
            
x_title = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT','SUN'] #요일 제목 저장

for i in range(0, 7) : #월~일요일까지 7번 반복
    for j in range(0, len(a[i])) : #데이터 수만큼 반복
        print(x_title[i], "[", j, "] = ", a[i][j]) #시간대별로 데이터 출력

