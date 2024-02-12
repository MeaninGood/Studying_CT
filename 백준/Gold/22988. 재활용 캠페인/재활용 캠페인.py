import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

s, e = 0, n - 1
x = n
cnt = 0
for i in range(n)[::-1] :
    if arr[i] == m :
        cnt += 1
        e = i - 1
        x = n - cnt

while s < e :
    if (2 * (arr[s] + arr[e])) >= m :
        cnt += 1
        x -= 2
        s += 1
        e -= 1
        
    else :
        s += 1

print(cnt + x // 3)