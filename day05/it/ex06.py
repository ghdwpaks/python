data1 = 3
data2 = 5

'''
data1 | data2
0011 (3)
0101 (5)
------
0111 (7)
'''
result = data1 | data2
print("{} | {} = {}".format(data1,data2,result))

'''
data1 & data2
0011 (3)
0101 (5)
------
0001 (1)
'''
result = data1 & data2
print("{} & {} = {}".format(data1,data2,result))


'''
data1 ^ data2
0011 (3)
0101 (5)
------
0110 (6)
'''
result = data1 ^ data2
print("{} ^ {} = {}".format(data1,data2,result))