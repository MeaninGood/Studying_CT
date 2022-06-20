import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

s = 0
e = 0
total = 1 << 30
while e < n and s <= e:
    if total >= abs(arr[e] - arr[s]) and abs(arr[e] - arr[s]) >= m:
        total = abs(arr[e] - arr[s])

    if abs(arr[e] - arr[s]) > m :
        s += 1
    
    else:
        e += 1
        
print(total)