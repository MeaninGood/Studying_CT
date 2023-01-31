import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()


# 0 위치 뽑기 (V)
def loc_zero(arr):
    zeros = []
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                zeros.append([i, j])
                
    return zeros
    
    
# 2 위치 뽑기
def loc_two(arr):
    twos = []
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                twos.append([i, j])
    
    return twos


# 벽 3개 세우기 - 조합
def recur(cur=0, num=0, tmp=[]):
    global answer
    if cur == 3:
        # tmp 좌표들 1로 만들기
        for x, y in tmp:
            arr[x][y] = 1
        # bfs 돌기 - 시작점이 여러 개인 좌표 동시에 넣고 한번에 돌기
        tmp2 = bfs()
        answer = max(answer, zero - tmp2)

        # tmp 원래대로 0으로 만들기
        for x, y in tmp:
            arr[x][y] = 0
        
        return 
    
    for i in range(num, len(zeros)):
        recur(cur + 1, i + 1, tmp + [zeros[i]])
    

# x, y 범위 체크 (V)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# bfs 돌아서 개수 리턴 (V)
def bfs():
    visited = [[False for _ in range(m)] for _ in range(n)]
    que = deque()
    
    for a, b in twos:
        que.append([a, b])
        visited[a][b] = True
    
    ret = 0
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 1:
                continue
            
            que.append([nx, ny])
            visited[nx][ny] = True
            ret += 1
                
    return ret
    
    
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

zeros = loc_zero(arr)
twos = loc_two(arr)
zero = len(zeros) - 3
answer = -1

recur()

print(answer)