Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>
from time import time

def getTime():
 return time() - float(str(time()).split('.')[0])

def getRange(minimum, maximum):
 return float(getTime() * (maximum - minimum) + minimum)

print(getRange(35,95))
