import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [0] + list(map(int, input().split()))
prefix = [0 for _ in range(n + 1)]

mx = -1 << 31
for i in range(1, n + 1):
    prefix[i] = max(prefix[i - 1] + arr[i], arr[i])
    mx = max(prefix[i], mx)
    
print(mx)