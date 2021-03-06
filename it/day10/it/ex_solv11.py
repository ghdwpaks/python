'''
string_data = "It is a fun Python CLASS" 다음 문자열 중에서
'a'의 갯수, 's'의 개수, 문자의 총 개수(공백 포함)도 구하시오.

총 개수 : 24
a 개수 : 2
s 개수 : 3

'''

string_data = "It is a fun Python CLASS"

for i in range (0 , len(string_data)) :
    print("string_data =",string_data[i])




'''선생님 답안'''
string_data = "It is a fun Python CLASS"
total = 0
a_count = 0
s_count = 0
for s in string_data :
    total += 1
    if s == 'a' or s == 'A' :
        a_count += 1
    elif s == 's' or s == "S" :
        s_count += 1

print("총 문자의 개수 : {}".format(total))
print("'a' 문자의 개수 : {}".format(a_count))
print("'s' 문자의 개수 : {}".format(s_count))



