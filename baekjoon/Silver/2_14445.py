import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())

arr = [0 for i in range(n + 1)]
for i in range(m):
    tmp = int(input())
    arr[tmp] = 1


s = 1
e = 1
ans = 100000
cnt = 1
tmp = arr[1]

while s <= e:
    if cnt >= k:
        ans = min(ans, tmp)
        
    if cnt <= k and e < n:
        e += 1
        tmp += arr[e]
        cnt += 1
        
    else:
        tmp -= arr[s]
        s += 1
        cnt -= 1

print(ans)