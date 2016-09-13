from sys import stdin
from sys import stdout
from collections import defaultdict

n = int(stdin.readline())
a = defaultdict(int)

for i in range(n):
    op, x = stdin.readline().split()
    m = int(''.join(('0' if ord(c) % 2 == 0 else '1') for c in x))
    if op == '?':
        stdout.write(str(a[m]) + '\n')
    else:
        a[m] += 1 if op == '+' else -1

stdout.flush()
