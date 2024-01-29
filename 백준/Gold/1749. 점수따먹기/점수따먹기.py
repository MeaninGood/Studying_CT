import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [[0 for _ in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0 for _ in range(m + 2)]] 

prefix = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
mx = -1 << 31
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
        for x in range(i):
            for y in range(j):
                mx = max(prefix[i][j] - prefix[x][j] - prefix[i][y] + prefix[x][y], mx)
        
print(mx)