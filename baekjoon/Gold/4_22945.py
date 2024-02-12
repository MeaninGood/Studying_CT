import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split())) + [0]

s, e = 0, n - 1
mx = -1

while s < e and e < n:
    total = (e - s - 1) * min(arr[s], arr[e])
    mx = max(total, mx)
    
    if arr[s] > arr[e]:
        e -= 1
        
    else:
        s += 1

print(mx)