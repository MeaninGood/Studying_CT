import sys
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
total = arr[0]
cnt = 1
mn = 1 << 31

while e < n:
    if total < k:
        cnt += 1
        e += 1
        total += arr[e]

    elif total >= k:
        mn = min(cnt, mn)
        