from os import path as os_path
PATH = os_path.abspath(os_path.split(__file__)[0])

print(PATH)

import os
a = os.getcwd()
print(a)

import sys
b=sys.argv
b = b[1:]
c= " ".join(b).lower().strip()
print(c)
e = c.split(" ")
print(e)
f= e[0].capitalize()
print(type(e[0]))
print(f)

print("e vaut : "+str(e))
print(f"e vaut : {str(e)}")