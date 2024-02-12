import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [0 for _ in range(m + 1)]
for i in range(n):
    a = int(input())
    if i % 2:
        arr[0] += 1
        arr[a] -= 1
    else:
        arr[m - a] += 1
        arr[m] -= 1

prefix = [0 for _ in range(m + 1)]
prefix[0] = arr[0]

mn = 1 << 31
for i in range(1, m):
    prefix[i] = prefix[i - 1] + arr[i]
    mn = min(mn, prefix[i])
    
ans = 0
for i in range(m):
    ans += (prefix[i] == mn)
print(mn, ans)