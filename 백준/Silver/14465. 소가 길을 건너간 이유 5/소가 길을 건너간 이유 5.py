import sys

input = lambda: sys.stdin.readline().strip()

n, k, b = map(int, input().split())
arr = [0 for _ in range(n + 1)]
for i in range(b):
    t = int(input())
    arr[t] = 1

arr += [0]

s, e = 1, 1
cnt = 1
length = arr[s]
ans = 1 << 31
while e < n + 1:
    if cnt >= k:
        ans = min(ans, length)
        length -= arr[s]
        s += 1
        cnt -= 1
        
    else:
        e += 1
        length += arr[e]
        cnt += 1
        
print(ans)