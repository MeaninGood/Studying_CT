# DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(cur):
    visited[cur] = True
    
    print(cur, end =' ')
        
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)
        
        
def bfs(s):
    que = deque()
    li = [False for i in range(n+1)]
    
    que.append(s)
    li[s] = True

    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            print(cur, end = ' ')
            
            for nxt in arr[cur]:
                if li[nxt]:
                    continue
                
                que.append(nxt)
                li[nxt] = True
        
        
n, m, v = map(int, input().split())

arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()
    

visited = [False for _ in range(n+1)]

dfs(v)
print()
bfs(v)



# 연결 요소의 개수

def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)


n, m = map(int, input().split())

v = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)
    
visited = [False for i in range(n+1)]

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)




# 단지 번호 붙이기

def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
   
def dfs(x, y):
    ret = 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not ( 0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] == '0':
            continue
        
        ret += dfs(nx, ny)
    
    return ret

n = int(input())
arr = [ input() for i in range(n) ]

visited = [[False for i in range(n)] for j in range(n)]
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or arr[i][j] == '0':
            continue
        
        cnt += 1
        ans.append(dfs(i, j))
        
print(cnt) # cnt 안 쓸 거면 len(ans)
ans.sort()
for i in ans:
    print(i)





# 노드의 거리(swea)

from collections import deque

def bfs(s):
    que = deque()
    visited = [False for i in range(n + 1)]
    
    que.append(s)
    visited[s] = True
    
    ret = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()
            
            if cur == e:
                return ret
            
            for nxt in v[cur]:
                if visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
        
        ret += 1        
    return 0

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    v = [[]for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        
        v[a].append(b)
        v[b].append(a)
 
    s, e = map(int, input().split())
    print(f'#{tc} {bfs(s)}')




# 미로 탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip())))
    
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    cnt = 0
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        cnt += 1
        
        for _ in range(size):
            x = que[0][0]
            y = que[0][1]
            que.popleft()
            
            if (x == n - 1) and (y == m - 1):
                return cnt
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 1 or visited[nx][ny]:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True               
    
print(bfs(0, 0))