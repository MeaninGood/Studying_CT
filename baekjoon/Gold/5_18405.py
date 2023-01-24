# 18405 - 경쟁적 전염

import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y, cnt):
    global ret

    que = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    que.append([x, y, cnt])
    visited[x][y] = True

    while que:
        size = len(que)
        ret = 100000

        for _ in range(size):
            x, y, cnt = que.popleft()

            if cnt > s:
                ret = 0
                return 0
                
            if arr[x][y] != 0:
                ret = min(ret, arr[x][y])

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not in_range(nx, ny) or visited[nx][ny]:
                    continue

                que.append([nx, ny, cnt + 1])
                visited[nx][ny] = True
        
        if ret != 100000:
            return

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())
m = len(arr[0])

bfs(a - 1, b - 1, 0)
print(ret)