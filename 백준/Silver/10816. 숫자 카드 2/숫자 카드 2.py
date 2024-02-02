import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
v = list(map(int, input().split()))

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
    
for i in v:
    if i in d:
        print(d[i], end = ' ')
    else:
        print(0, end = ' ')