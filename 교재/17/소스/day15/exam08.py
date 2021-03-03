'''
리스트 sort(), reverse()
sort() : 오름차순 또는 내림차순 정렬, 기본 값 오름차순
'''

list_data = [10, 30, 20]
print('reverse() 호출 전 : ', list_data)
print('reverse() 반환 값 : ', list_data.reverse()) 
# list_data.reverse()
print('reverse() 호출 후 : ', list_data)

# 오름차순
list_data = [4,8,7,2,6]
print('sort() 호출 전 : ', list_data)
print('sort() 반환 값 : ', list_data.sort()) 
print('sort() 호출 후 : ', list_data)
print()
#내림차순
list_data = [4,8,7,2,6]
print('sort() 호출 전 : ', list_data)
print('sort() 반환 값 : ', list_data.sort(reverse=True)) 
print('sort() 호출 후 : ', list_data)