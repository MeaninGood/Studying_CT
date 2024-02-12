import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

s, e = 0, n - 1
x, y = arr[0], arr[n - 1]
while s < e:
    target = x + y
    total = arr[s] + arr[e]
    
    if abs(total) < abs(target):
        x, y = arr[s], arr[e]
        
    elif total < 0:
        s += 1
        
    else:
        e -= 1
        
print(min(x, y), max(x, y))