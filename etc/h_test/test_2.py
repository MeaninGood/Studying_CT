import sys
from collections import deque
from pprint import pprint
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < 8 and 0 <= y < 8    
    
bishop1 = ["C6"]
bishops = ["C6", "A4", "E5"]
chess = [[False for _ in range(8)] for _ in range(8)]

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]


arr = []
for i in range(len(bishops)):
    arr.append([ord(bishops[i][0]) - ord('A'), int(bishops[i][1]) - 1])

visited = [[False for i in range(8)] for j in range(8)]

arr.sort()
cnt = 0
for k in range(len(arr)):
    x, y = arr[k][0], arr[k][1]
    
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 1:
            if not in_range(nx, ny) or visited[nx][ny] or [nx, ny] in arr:
                break

            cnt += 1
            visited[nx][ny] = True
            nx += dx[i]
            ny += dy[i]

print(64 - cnt)