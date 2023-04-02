import sys
from itertools import combinations
from collections import deque
input = lambda : sys.stdin.readline().strip()

def check(tmp_arr):
    cnt = 0
    for x, y in tmp_arr:
        if arr[x][y] == 'S':
           cnt += 1
           
    return cnt >= 4

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(tmp_arr):
    que = deque()
    visited = [False for _ in range(7)]
    
    que.append(tmp_arr[0])
    visited[0] = True
    
    while que:
        x, y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if [nx, ny] not in tmp_arr:
                continue
            
            nxt = tmp_arr.index([nx, ny])
            
            if visited[nxt]:
                continue
            
            que.append([nx, ny])
            visited[nxt] = True
                    
    return False not in visited

tmp_idx = [[i, j] for i in range(5) for j in range(5)]

arr = [list(input()) for _ in range(5)]
v = list(combinations(tmp_idx, 7))
n = len(v)

answer = 0
for i in v:
    if check(i):
        answer += bfs(i)
    
print(answer)