from array import array
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr = arr[::-1]

cnt = 0
i = 0
while i < n - 1:
    if arr[i] <= arr[i + 1] and arr[i + 1] > 1:
        arr[i + 1] -= 1
        cnt += 1
    
    else:
        i += 1
    
print(cnt)