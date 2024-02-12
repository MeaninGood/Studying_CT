import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split())) + [0]


s, e = 0, 0
length = 0 if arr[s] % 2 == 1 else 1
cnt = arr[s] % 2
mx = 0
while e < n:
    if cnt <= k:
        mx = max(length, mx)
        e += 1
        cnt += arr[e] % 2
        length += 0 if arr[e] % 2 == 1 else 1
    else:
        length -= 0 if arr[s] % 2 == 1 else 1
        cnt -= arr[s] % 2
        s += 1
        
print(mx)