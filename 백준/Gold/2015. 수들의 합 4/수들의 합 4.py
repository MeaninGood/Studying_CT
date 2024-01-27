import sys
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n)]
prefix[0] = arr[0]

for i in range(1, n):
    prefix[i] = prefix[i - 1] + arr[i]

d = {}
ans = 0
for i in range(n):
    if prefix[i] == k:
        ans += 1
    target = prefix[i] - k
    ans += d.get(target, 0)
    d[prefix[i]] = d.get(prefix[i], 0) + 1

print(ans)