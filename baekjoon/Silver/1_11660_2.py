import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [[0 for _ in range(n + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]  +  [[0 for _ in range(n + 2)]] 

prefix = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    # 전체 - 구간1 - 구간2 + 구간12교집합
    total = prefix[x2][y2]
    sec1 = prefix[x2][y1 - 1]
    sec2 = prefix[x1 - 1][y2]
    inter = prefix[x1 - 1][y1 - 1]
    print(total - sec1 - sec2 + inter)