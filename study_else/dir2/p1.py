
import random
def password(length) :
	pw = str() # str() 빈 문자열 생성
	chars = 'abcdefghhijklmnopqrstuvwxyz' + '0123456789' + '!@#$%^&*'
	for i in range(0,length) :
		pw = pw + random.choice(chars)
	return pw

print(password(8))
