import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def check(x):
    total = 0
    for i in range(n):
        total += arr[i] // x
        
    return total >= m


s, e = 1, 1 << 31
ans = 0
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        s = mid + 1
        
    else:
        e = mid - 1
        
print(ans)