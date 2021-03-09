def func1() :
    data1 = 100 # local variable(지역변수)
    print('func1() data : {} '.format(data1))

def func2() :
    data2 = 200
    print('func1() data : {} '.format(data2))

data = 200 # global variable(전역변수)
func1()
func2()
print(data)
# print(data1) 에러
# print(data2) 에러
