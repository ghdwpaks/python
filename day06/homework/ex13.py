i = True
ii = False

print("True or True: {}".format(i or i))
print("True or False: {}".format(i or ii))
print("False or True: {}".format(ii or i))
print("False or False: {}".format(ii or ii))
print()

print("True and True: {}".format(i and i))
print("True and False: {}".format(i and ii))
print("False and True: {}".format(ii and i))
print("False and False: {}".format(ii and ii))
print()

print("Not True = {}".format(not(i)))
print("Not False = {}".format(not(ii)))
print()
