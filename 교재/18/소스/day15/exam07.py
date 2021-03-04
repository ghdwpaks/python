'''
리스트 pop(), remove(), clear()
pop() : 인덱스를 기준으로 데이터 삭제
remove() : 데이터를 기준으로 삭제
clear() : 모두 다 삭제
'''

list_data = [10, 20, 30]
print('pop() 호출 전 : ', list_data)
print('pop() 반환 값 : ', list_data.pop()) # 마지막 데이터를 반환해요
print('pop() 호출 후 : ', list_data)

list_data = [10, 20, 30]
print('pop() 호출 전 : ', list_data)
print('pop() 반환 값 : ', list_data.pop(0)) # 0번 인덱스의 값을 반환해요
print('pop() 호출 후 : ', list_data)

list_data = [10, 20, 30]
print('pop() 호출 전 : ', list_data)
print('pop() 반환 값 : ', list_data.pop(1)) # 1번 인덱스의 값을 반환해요
print('pop() 호출 후 : ', list_data)

list_data = [10, 20, 30]
print('pop() 호출 전 : ', list_data)
print('pop() 반환 값 : ', list_data.pop(0))
print('pop() 반환 값 : ', list_data.pop(0))
print('pop() 반환 값 : ', list_data.pop(0))
print('pop() 호출 후 : ', list_data)

# 없는 인덱스로  에러
# list_data = [10, 20, 30]
# print('pop() 호출 전 : ', list_data)
# print('pop() 반환 값 : ', list_data.pop(10)) 

list_data = [10, 20, 30]
print('remove() 호출 전 : ', list_data)
print('remove() 반환 값 : ', list_data.remove(10)) 
print('remove() 호출 후 : ', list_data)

list_data = [10, 20, 30]
print('remove() 호출 전 : ', list_data)
print('remove() 반환 값 : ', list_data.remove(20)) 
print('remove() 호출 후 : ', list_data)

# 없는 데이터는 에러
# print('remove() 호출 전 : ', list_data)
# print('remove() 반환 값 : ', list_data.remove(20)) 
# print('remove() 호출 후 : ', list_data)

list_data = [10, 20, 30]
print('clear() 호출 전 : ', list_data)
print('clear() 반환 값 : ', list_data.clear()) 
print('clear() 호출 후 : ', list_data)