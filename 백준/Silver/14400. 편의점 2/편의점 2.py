import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

arr.sort()
nx = arr[n // 2][0] if n % 2 else arr[n // 2 - 1][0]

arr.sort(key = lambda x: x[1])
ny = arr[n // 2][1] if n % 2 else arr[n // 2 - 1][1]

total = 0
for x, y in arr:
    total += abs(x - nx) + abs(y - ny)
    
print(total)