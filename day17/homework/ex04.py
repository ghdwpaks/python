import copy
m = {}
d = {"name" : "ghdwpaks", "age" : 18,"school" :"한세" }
name = "ghdwpaks"
print(d)
print(d.get("name"))


m[1] = copy.deepcopy(d)
print("m :",m)
t = (m.get(1)).get('name')
print(t)
print(t.get("name"))
