code = "for i in range(1,10):print(i)"
cmpcode = compile(code, 'a.py', 'exec')
a = 100
eval(cmpcode)


str1 = "aaa"
str2 = str1 + "bbb"
print(str2)