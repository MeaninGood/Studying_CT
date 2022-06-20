import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

s = 0
e = len(arr) - 1
x, y = 0, 0

total = 10000000000
while s < e:
    if abs(total) > abs(arr[s] + arr[e]):
        total = arr[s] + arr[e]
        x, y = arr[s], arr[e]
        
    if arr[s] + arr[e] < 0:
        s += 1
        
    else:
        e -= 1

ans = [x, y]
ans.sort()
print(*ans)