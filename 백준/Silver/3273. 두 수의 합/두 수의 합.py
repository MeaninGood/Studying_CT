import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()


s, e = 0, n - 1

ans = 0
while s < e:
    if arr[s] + arr[e] == x:
        ans += 1
        s += 1

    elif arr[s] + arr[e] < x:
        s += 1
        
    else:
        e -= 1
        
print(ans)