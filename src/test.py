def HexToString(s):
    n = 2
    return "".join([chr((int(s[i:i + n], 16)) % 256) for i in range(0, len(s) - n + 1, n)])

s = '70726F6772616D6D6572'
print HexToString(s);