
s = input("아무 문장 입력 : ")
spe = [['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']]
spec = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#print(len(spe[0]))

for i in range (0 , len(s)) :
    #print("s =",s[i])
    for j in range (0 , len(spe[0])) :
        if s[i] == spe[0][j] or s[i] == spe[1][j]:
            spec[j] += 1

for i in range(0,len(spec)) :
    if spec[i] != 0 :
        print("{} = {}개".format(spe[0][i],spec[i]))
    