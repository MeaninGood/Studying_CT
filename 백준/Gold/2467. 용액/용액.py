import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

s, e = 0, n - 1
mn = 1 << 31
x, y = arr[s], arr[e]
while s < e:
    total = arr[e] + arr[s]
    if abs(total) < mn:
        mn = abs(total)
        x, y = arr[s], arr[e]
        
    elif total < 0:
        s += 1
        
    else:
        e -= 1
        
print(min(x, y), max(x, y))