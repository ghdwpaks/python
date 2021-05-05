# -*- coding: utf-8 -*- 
import js2py 
a = input("계산식 : ")
b = js2py.eval_js(a) 
print("결과 :",b)

