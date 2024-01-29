import sys

input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr += [0]

s, e = 0, 0 
total = arr[s]
length = 1
cnt = 0
ans = 1 << 31
while e < n:
    if total >= k:
        cnt += 1
        ans = min(length, ans)
        total -= arr[s]
        s += 1
        length -= 1
        
    else:
        e += 1
        total += arr[e]
        length += 1
        

print(ans if cnt else 0)