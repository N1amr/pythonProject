x = 1234;

def factorial(x):
    r = 1;
    for i in xrange(1, x + 1):
        r = r * i;
    return r;

def f(x):
    r = 1;
    s = list(str(x));
    for c in s:
        C = int(str(c))
        r = r * factorial(C)
    return r

print f(734)
print f(9)

# for d in range(8, 10):
#     i = 10000000
#     while i > 5000:
#         if(f(d) == f(i) and not('1' in list(str(i))) and not('0' in list(str(i)))):
#             print str(d) + " >> " + str(i);
#         i=i-1    
