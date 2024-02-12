import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [-1 << 31] + list(map(int, input().split())) + [1 << 31]

idx, cnt = 0, 0
for i in range(1, n + 1):
    if arr[i - 1] > arr[i]:
        idx = i
        cnt += 1
        
    if cnt >= 2:
        print(0)
        exit()


if cnt == 0:
    print(n)
else:
    print((arr[idx - 2] <= arr[idx]) + (arr[idx - 1] <= arr[idx + 1]))