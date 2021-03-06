'''
세 자리의 수 중 1,2,3으로 구성된 수들을
오름차순 나열 했을 때, 14 번째 위치한 수를 출력 하시오.
예)111,112,113,121...

'''

count = 0
for i in range(1 , 4) :
    for j in range(1,4) :
        for k in range(1, 4) :
            count +=1
            print("{}".format(i*100+j*1+k))
            if count == 14 :
                print("{}".format(i*100+j*1+k))
                break
