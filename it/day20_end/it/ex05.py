def fu(a) :
    return a ** a

l = [fu,2]
r = l[0](l[1])
print(r)