l1 = [1,2,3]
#[1,2,3]이라는 데이터를 '가리키는'객체인 l1과

l2 = l1
#[1,2,3]이라는 데이터를 '가리키는'객체인 l2가 있다.

print(l1)
print(l2)
print("=========")
#근데 l1이라는 객체를 통해서 [1,2,3]이라는 데이터를 지우니
l1.clear()
print(l1)
print(l2)
#[1,2,3]을 가리키는 l2라는 객체도 아무것도 출력하지 않게 된다.

