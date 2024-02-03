import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def check(x):
    total = 0
    for i in arr:
        total += max(i - x, 0)
        
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