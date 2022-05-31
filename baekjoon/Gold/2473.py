import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
    
x, y, z = arr[0], arr[1], arr[2]
for i in range(n - 2):
    idx = i
    s = idx + 1
    e = n - 1
    while s < e:
        total = arr[idx] + arr[s] + arr[e]
        if abs(total) < abs(x + y + z):
            x = arr[idx]
            y = arr[s]
            z = arr[e]
            
        if total < 0:
            s += 1
            
        else:
            e -= 1
            
print(x, y, z)