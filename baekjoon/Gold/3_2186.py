# 2186 - 문자판

import sys
from pprint import pprint
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, tmp, cnt):
    if dp[x][y][cnt] != -1:
        return dp[x][y][cnt]

    if len(tmp) >= len(idx):
        return 1
    dp[x][y][cnt] = 0

    for i in range(1, k+1):
        for j in range(4):
            nx = x + (dx[j] * i)
            ny = y + (dy[j] * i)

            if not in_range(nx, ny) or (arr[nx][ny] != idx[cnt + 1]):
                continue
            
            dp[x][y][cnt] += dfs(nx, ny, tmp + arr[nx][ny], cnt + 1)

    return dp[x][y][cnt]

n, m, k = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]
idx = input()
dp = [[[-1 for i in range(90)] for j in range(110)] for k in range(110)]

total = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == idx[0]:
            total += dfs(i, j, arr[i][j], 0)

print(total)