x = 10
print(x)
def fun():
    global x    # x를 전역 변수로 만듦
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력

print(x)        # 전역 변수 출력 
fun()
print(x)        # 전역 변수 출력