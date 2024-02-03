import sys
si = sys.stdin.readline

def check(x):
    total = 0
    for i in range(n):
        if x >= arr[i][0]:
            total += ((min(arr[i][1], x) - arr[i][0]) // arr[i][2]) + 1
        
    return total


n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]

ans = 0
s = 0
e = 10000000000
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