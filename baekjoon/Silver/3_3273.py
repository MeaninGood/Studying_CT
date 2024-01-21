import sys

input = lambda : sys.stdin.readline().strip()

n= int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

s, e = 0, n - 1
cnt = 0
while s < e:
    if arr[s] + arr[e] == x:
        cnt += 1
        s += 1
        e -= 1
        
    elif arr[s] + arr[e] < x:
        s += 1
        
    else:
        e -= 1
        
print(cnt)