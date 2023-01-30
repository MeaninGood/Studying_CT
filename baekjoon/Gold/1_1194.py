# 굿
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

def num(a):
    return 1 << (ord(a) - ord('A'))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y, keys):
    que = deque()
    visited = [[[False for _ in range(64)] for i in range(m)] for j in range(n)]

    que.append([x, y, keys])
    visited[x][y][0] = True

    ret = 0
    while que:
        size = len(que)
        for _ in range(size):
            x, y, keys = que.popleft()

            if arr[x][y] == '1':
                return ret
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or arr[nx][ny] == '#' or visited[nx][ny][keys]:
                    continue

                elif ord('a') <= ord(arr[nx][ny]) <= ord('z'):
                    if num(arr[nx][ny].upper()) & keys:
                        que.append([nx, ny, keys])
                        visited[nx][ny][keys] = True
                    else:
                        tmp = keys | num(arr[nx][ny].upper())
                        que.append([nx, ny, tmp])
                        visited[nx][ny][tmp] = True

                elif (ord('A') <= ord(arr[nx][ny]) <= ord('Z')) and (keys & num(arr[nx][ny].upper())):
                    que.append([nx, ny, keys])
                    visited[nx][ny][keys] = True

                elif arr[nx][ny] == '.' or arr[nx][ny] == '0' or arr[nx][ny] == '1':
                    que.append([nx, ny, keys])
                    visited[nx][ny][keys] = True

        ret += 1
    return -1


sx, sy = 0, 0
end = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            sx, sy = i, j

        if arr[i][j] == '1':
            end.append([i, j])
ret = 0


print(bfs(sx, sy, 0))