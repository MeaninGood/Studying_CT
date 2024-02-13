import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

total = 0
for i in range(0, n, 2):
    total += arr[i]

mx, ans = total, total
for i in range(n - 1, -1, -2):
    mx += arr[i] - arr[i - 1]
    ans = max(ans, mx)

mx = total
for i in range(n - 2, 0, -2):
    mx += arr[i - 1] - arr[i]
    ans = max(ans, mx)

print(ans)