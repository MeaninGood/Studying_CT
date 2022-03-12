# 11660 구간 합 구하기 5

n, m = map(int, input().split())
arr = [[0 for i in range(n + 1)] + [0] + list(map(int, input().split())) for i in range(n)]
prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
for _ in range(m):
    a, b, c, d = map(int, input().split())
    
    print(prefix[c][d] - prefix[a - 1][d] - prefix[c][b - 1] + prefix[a - 1][b - 1])
    
    

import sys

n = int(sys.stdin.readline())
arr = [[0 for i in range(n + 1)] + [0] + list(map(int, sys.stdin.readline().split())) for j in range(n)]
prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]


q = int(sys.stdin.readline())
