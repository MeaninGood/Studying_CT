import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
k = int(input())


def check(a):
    total = 0
    for i in range(1, n + 1):
        total += min(n, a // i)
        
    return total >= k

s, e = 0, n * n
ans = 0
while s <= e:
    mid = (s + e) // 2
    if check(mid):
        ans = mid
        e = mid - 1
        
    else:
        s = mid + 1
        
print(ans)