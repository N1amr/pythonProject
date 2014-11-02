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

h = '696E746572657374656420696E2073656375726974792C63727970746F6772617068792C7068696C6F736F7068792C706879736963732C617374726F6E6F6D79'
b = '010111000101110000110000'
s = 'If you can read this, you are smart'
ss = 'abx'
print (ss)
print (StringToHex(s))
print HexToString(h)
print (HexToString(BinaryToHex(b)))
