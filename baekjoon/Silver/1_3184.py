import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    que = deque()
    
    visited[x][y] = True
    que.append([x, y])
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited:
                    pass
    

n, m = map(int, input().split())
arr = [list(map(str, input())) for _ in range(n)]

visited = [[False for i in range(m)] for j in range(n)]