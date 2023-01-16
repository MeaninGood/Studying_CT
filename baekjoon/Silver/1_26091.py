import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

if n == 1:
    print(0)
    exit()
    
s = 0
e = n - 1
total = 0
while e > s:
    if arr[s] + arr[e] >= m:
        total += 1
        e -= 1
        s += 1
    
    else:
        s += 1
        
print(total)