dict_data = {'key01': 1,'key02': 2,'key03': 3,'key04': 4}

print("dict_data.keys() : ",dict_data.keys())
print("dict_data.keys() : ",list(dict_data))
print("dict_data.keys() : ",list(dict_data.keys()))
print()
print()

print("dict_data.values() : ",dict_data.values())
print("dict_data.values() : ",list(dict_data))
print("dict_data.values() : ",list(dict_data.values()))

for key in dict_data.keys() :
    print(key)

for value in dict_data.values() :
    print(value)
print(dict_data.items())
for key,value in dict_data.items() :
    print(key,":",value)
