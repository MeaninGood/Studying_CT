import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

def check(x):
    total = 0
    
    for i in range(m):
        total += arr[i] // x
        
        if arr[i] % x:
            total += 1
            
    return total <= n


s, e = 1, 1 << 31
ans = 0
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        e = mid - 1
        
    else:
        s = mid + 1
        
print(ans)