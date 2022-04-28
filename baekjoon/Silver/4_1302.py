import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
    
print(max(d))