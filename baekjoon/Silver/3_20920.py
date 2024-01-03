import sys

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())

arr = [input() for _ in range(n)]

d = {}
for i in arr:
    if len(i) < m:
        continue

    d[i] = d.get(i, 0) + 1

tmp = list(d.items())

tmp.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for x, y in tmp:
    print(x)
