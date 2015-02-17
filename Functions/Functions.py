# Primes
primeFlags = [False, False]
def initPrimes(n):
    for i in range(n - 2):
        primeFlags.append(True);
    for i in range(2, n):
        if(primeFlags[i] == True):
            for j in range (2 * i, n, i):
                primeFlags[j] = False;

def isPrime(n):
    return primeFlags[n]

# Primes 2
def initPrimes(n):
    primeFlags = n * [True]
    primeFlags[0] = False
    primeFlags[1] = False
    for i in range(2, n):
        if(primeFlags[i] == True):
            for j in range (2 * i, n, i):
                primeFlags[j] = False;
    return primeFlags

def isPrime(n):
    return primeFlags[n]


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
