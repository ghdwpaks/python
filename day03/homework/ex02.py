dict1 = {}
dict1 = {
    'py':{"score":98, "class_time":40},
    'C_lang' :{"score":90, "class_time":48},
    "java" : {"score":88, "class_time":50}
}
for i in dict1 : print(i)

#이거 dict1 안에 있는 내용물 하나도 빠짐없이 출력하는거 만들어보기
print(dict1["py"])
print(dict1["C_lang"])
print(dict1["java"])
print()

print(dict1["py"]["score"])
print(dict1["py"]["class_time"])
print()
print(dict1["C_lang"]["score"])
print(dict1["C_lang"]["class_time"])
print()
print(dict1["java"]["score"])
print(dict1["java"]["class_time"])
print()


print('\n\n분기점\n\n')

dict2 = {
    "dict2_1":dict1,
    "dict2_2":{
        "math":{"score":70, "class_time":80},
        "eng":{"score":83, "class_time":45,"toeic":800}
    }
}
print(dict2)
print()
print(dict2["dict2_1"])
print()
print(dict2["dict2_2"]["math"])
print()
print(dict2["dict2_2"]["math"]["score"])
