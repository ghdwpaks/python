def func1() :
    data = 100 # local variable(지역변수)
    print('func1() data : {} '.format(data))

def func2() :
    print('func1() data : {} '.format(data))

data = 200 # global variable(전역변수)
func1()
func2()