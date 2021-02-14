in1 = int(input("숫자입력1 : "))
in2 = int(input("숫자입력2 : "))

print("{} > {} = {}".format(in1,in2, in1 > in2))
print("{} >= {} = {}".format(in1,in2, in1 >= in2))
print("{} != {} = {}".format(in1,in2, in1 != in2))
print("{} == {} = {}".format(in1,in2, in1 == in2))
print("{} < {} = {}".format(in1,in2, in1 < in2))
print("{} <= {} = {}".format(in1,in2, in1 <= in2))
print()

result = False
i = 0
k_reuslt = "거짓"
while(i < 6) :
    if i == 0 :
        result = in1 > in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} > {} = {}".format(in1,in2, k_reuslt))
    elif i == 1 : 
        reuslt = in1 >= in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} >= {} = {}".format(in1,in2, k_reuslt))
    elif i == 2 :
        result = in1 != in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} != {} = {}".format(in1,in2, k_reuslt))
    elif i == 3 :
        result = in1 == in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} == {} = {}".format(in1,in2, k_reuslt))
    elif i == 4 :
        result = in1 < in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} < {} = {}".format(in1,in2, k_reuslt))
    elif i == 5 :
        result = in1 <= in2
        if result :
            k_reuslt = "진실"
        else : 
            k_reuslt = "거짓"
        print("{} <= {} = {}".format(in1,in2, k_reuslt))
    i += 1




