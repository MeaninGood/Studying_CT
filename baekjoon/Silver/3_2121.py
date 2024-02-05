import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

d = {}
for x, y in arr:
    d[(x, y)] = d.get((x, y), 0) + 1

ans = 0
for x, y in arr:
    if d.get((x + a, y)) and d.get((x, y + b)) and d.get((x + a, y + b)):
        ans += 1
        
print(ans)