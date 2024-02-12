import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i]
    
for i in range(m):
    a, b = map(int, input().split())
    
    print(prefix[b] - prefix[a - 1])