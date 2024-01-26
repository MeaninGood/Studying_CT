import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i]
    
mx = -1 << 31
for i in range(k, n + 1):
    mx = max(prefix[i] - prefix[i - k], mx)
    
print(mx)