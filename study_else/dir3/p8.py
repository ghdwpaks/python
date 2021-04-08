
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
sum = 0
for i in range(len(fruitdb)) :
	sum += fruitdb[i][1]
avg = sum/len(fruitdb)
print('%.1f원' % avg)
