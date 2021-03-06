import copy
c = 0 #all count
ops = []
tmp = {}
ibs = """
jo 1922-02-22
cho 1990-04-02
park 2012-12-12
lee 1998-09-08
kim 1990-05-14
"""
ibs = ibs.strip()
ibs_t = ibs.split('\n')
print("ibs_t",ibs_t)
for i in range(0,len(ibs_t)) :
    
    '''
    print("입력 예시) jo 1922-02-22")
    u = input("입력 : ")
    '''
    ibs_t[i].strip()
    name, born = ibs_t[i].split(" ")
    print("name :",name)
    print("born :",born)
    y,m,d = born.split("-")
    tmp["name"] = name
    tmp["y"] = y
    tmp["m"] = m 
    tmp["d"] = d
    t = copy.deepcopy(tmp)
    ops.append(t)
print("ops",ops)

for i in ops :
    #print("i =",i)
    print("{}님의 생일 {}년 {}월 {}일".format(i["name"],i['y'],i['m'],i['d']))



