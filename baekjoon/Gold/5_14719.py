import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [arr[0] for _ in range(m)]
for i in range(1, m):
    prefix[i] = max(prefix[i - 1], arr[i])
    
suffix = [arr[-1] for _ in range(m)]
for i in range(m - 1)[::-1]:
    suffix[i] = max(suffix[i + 1], arr[i])
    
ans = 0
for i in range(m):
    ans += min(prefix[i], suffix[i]) - arr[i]
    
print(ans)