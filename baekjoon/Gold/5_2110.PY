import sys
input = sys.stdin.readline


def check(x):
    idx = arr[0]
    cnt = 0
    for i in range(1, n):
        if idx + x <= arr[i]:
            cnt += 1
            idx = arr[i]

    return cnt >= (m - 1)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

ans = 0
s = 0
e = 100000000000

while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        s = mid + 1
    
    else:
        e = mid - 1
        
print(ans)