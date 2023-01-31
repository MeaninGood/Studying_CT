import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


# 0 & 2 위치 찾기
def find_nums(arr):
    zeros = []
    twos = []
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                zeros.append([i, j])
            if arr[i][j] == 2:
                twos.append([i, j])
                
    return zeros, twos


# 벽 세울 공간 3개 고르기 -(현재 노드, 시작 노드, 공간 3개 뽑은 배열[])
def recur(cur, s, tmp):
    global mx
    
    if cur == 3:
        # 벽 3개 세우기
        for a, b in tmp:
            arr[a][b] = 1
        
        # 모든 0의 개수 - 3개 // 벽은 무조건 3개이므로
        # - 바이러스 침투한 곳
        mx = max(mx, len(zeros) - bfs() - 3)
        
        # 벽 되돌리기
        for a, b in tmp:
            arr[a][b] = 0
    
        return
    
    for i in range(s, len(zeros)):
        recur(cur + 1, i + 1, tmp + [zeros[i]])


# bfs 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# bfs 돌기
def bfs():
    visited = [[False for i in range(m)] for j in range(n)]
    que = deque()
    
    # 처음에 바이러스 있는 곳(2인 곳) 다 넣어서 한번에 돌리기
    for a, b in twos:
        visited[a][b] = True
        que.append([a, b])
        
    ret = 0
    while que:
        x, y = que.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 1:
                continue
            
            visited[nx][ny] = True
            que.append([nx, ny])
            ret += 1
            
    return ret
    


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


mx = -100000
zeros, twos = find_nums(arr)
recur(0, 0, [])
print(mx)