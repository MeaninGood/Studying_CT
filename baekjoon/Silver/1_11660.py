import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, si().split())) for _ in range(n)]
prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, si().split())
    
    print(prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1])
    