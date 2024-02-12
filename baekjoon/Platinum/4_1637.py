import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def check(x):
    total = 0
    for a, c, b in arr:
        if x >= a:
            total += ((min(c, x) - a) // b) + 1
    
    return total


ans = 0
s, e = 0, 1 << 31
flag = False
while s <= e:
    mid = (s + e) // 2
    
    if check(mid) % 2:
        ans = mid
        e = mid - 1
        flag = True
        
    else:
        s = mid + 1
        
if flag:
    print(ans, check(ans) - check(ans - 1))
else:
    print('NOTHING')