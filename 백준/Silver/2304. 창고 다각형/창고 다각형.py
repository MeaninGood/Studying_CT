import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

m = 1010

arr = [0 for _ in range(m)]

for i in range(n):
    a, b = map(int, input().split())
    arr[a] = b
    
prefix = [0 for _ in range(m)]
for i in range(1, m):
    prefix[i] = max(prefix[i - 1], arr[i])
    

suffix = [0 for _ in range(m)]
for i in range(0, m - 1)[::-1]:
    suffix[i] = max(suffix[i + 1], arr[i])
    
ans = 0
for i in range(m):
    ans += min(prefix[i], suffix[i])
    
print(ans)