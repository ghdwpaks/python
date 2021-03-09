def func1() :
    global data1 # global variable(전역변수)
    data1 = 100
    print('func1() data : {} '.format(data1))

def func2() :
    data2 = 200 # loval variable(지역 변수)
    print('func1() data : {} '.format(data2))

data = 200 # global variable(전역변수)
func1()
func2()
print(data)
print(data1) 
# print(data2) 
