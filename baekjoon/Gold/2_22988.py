import sys

input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s, e = 0, n - 1
x = n
cnt = 0

for i in range(n)[::-1]:
    if arr[i] == m:
        cnt += 1
        e = i - 1
        x = n - cnt