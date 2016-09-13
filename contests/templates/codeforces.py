import sys

if sys.argv[0].count('/mnt/Storage'):
    sys.stdin = open('input')
    sys.stdout = open('output', 'w')

n = int(input())
a = list(map(int, input().split()))
print(a)
print(sum(a))