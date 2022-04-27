import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

mx = -1000000000
mn = 100000000
for i in range(n):
    mx = max(mx, arr[i])
    mn = min(mn, arr[i])
    
print(mx * mn)