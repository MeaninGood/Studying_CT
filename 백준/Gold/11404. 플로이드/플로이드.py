import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            arr[i][j] = 0
        
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b], c)
    
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            
            
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            print(0, end = " ")
            
        else:
            print(arr[i][j], end = " ")
    print()