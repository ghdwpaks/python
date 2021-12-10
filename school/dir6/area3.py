import area2 as a

a.print_area(10,20)
a.print_area(20,30)

for i in range(11,15) :
    a.print_area(i,20)

print("가로 30 세로 10 인 사각형의 넓이는",a.box_area(30,10))

print(a.__name__)


