# coding: UTF-8
from string import upper
def HexToString(h):
    n = 2
    try:
        return "".join([chr(int(h[i:i + n], 16)) for i in range(0, len(h) - n + 1, n)])
    except:
        return None
def StringToHex(s):
    n = 2
    try:
        return upper("".join([hex(ord(c))[2:] for c in s]))
    except:
        return None
    
def BinaryToHex(b):
    r = hex(int(b, 2))[2:]
    if(r[-1] == 'L'):
        r = r[:-1]
    return r

h = '49207468696E6B206974207761736E2774206861726420746F20726561642074686973203A44'
b = '010111000101110000110000'
s = "I think it wasn't hard to read this :D"
print (StringToHex(s))
print HexToString(h)
print (HexToString(BinaryToHex(b)))
