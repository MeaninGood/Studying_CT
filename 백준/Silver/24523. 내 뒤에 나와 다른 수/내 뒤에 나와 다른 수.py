import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

prefix = [-1 for _ in range(n + 1)]
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        prefix[i] = i + 1

tmp = -1
for i in range(n + 1)[::-1]:
    if i == n:
        continue
    if prefix[i] != -1:
        tmp2 = prefix[i]
        prefix[i] = tmp
        tmp = tmp2

    elif prefix[i] == -1:
        prefix[i] = tmp

print(*prefix[:-1])