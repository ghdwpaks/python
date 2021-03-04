'''
1       2       3       4       5
2       4       6       8       10
3       6       9       12      15
4       8       12      16      20
5       10      15      20      25
'''
for i in range(1, 6) :
    for j in  range(1,6) :
        print('{}\t'.format(i*j), end='')
    print()

print()
print()
'''
1       2       3       4       5
6       7       8       9       10
11      12      13      14      15
16      17      18      19      20
21      22      23      24      25
'''

for i in range(5) :
    for j in range(1, 6) :
        print('{}\t'.format( (i*5)+j ), end='')
    print()