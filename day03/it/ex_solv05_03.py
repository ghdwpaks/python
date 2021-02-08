'''
출발역에서 도착역까지 11개의 지하철 역을 지나왔다.
총 37분이 걸렸다면 한 역을 지나는데 걸리는 시간을 구해서 출력하시오.
'''
time = 37
station = 11
time_take_one_station = time / station

print("총 걸린 시간 : {}분".format(time))
print("거친 역의 갯수 : {}개".format(station))
print("한 역을 지나는데 걸리는 시간(분) : {:.2f}".format(time_take_one_station))
print()

'''선생님 풀이'''

total_station = 11
total_minute = 37
average_time = total_minute / total_station
print('한 역의 평균 시간은 {:.2f}분 입니다.'.format(average_time))