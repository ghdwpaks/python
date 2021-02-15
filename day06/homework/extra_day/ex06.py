in1 = 10
inf1 = 100.12345

print("변수 표현은 'in1 = {}'이렇게 표현할 수도 있지만,".format(in1))
print("in1 = %d 이렇게 표현할 수도 있습니다." % (in1))

print("inf1 = %.2f" % (inf1))
print("inf1 = {:f}".format(inf1))
print("inf1 = {:.3f}".format(inf1))


print('%10d원'%(1000))
print('%10d원'%(100000))
print('{:10}원'.format(100000))
print('{:10}원'.format(10000000))

print('%10s, %-10s'%('오른쪽','왼쪽'))
print('{:>10}, {:<10}'.format('오른쪽','왼쪽'))
print("{:^10}".format('가운데'))