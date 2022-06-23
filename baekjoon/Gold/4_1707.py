import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    que = deque()
    
    que.append(cur)
    visited[cur] = 0
    
    cnt = 0
    while que:
        size = len(que)
        cnt += 1
        
        for _ in range(size):
            cur = que.popleft()
        
            for nxt in v[cur]:
                if visited[nxt] == visited[cur]:
                    return False
                
                if visited[nxt] == -1:
                    que.append(nxt)
                    
                    if cnt % 2:
                        visited[nxt] = 1
                    
                    elif cnt % 2 == 0:
                        visited[nxt] = 0
     
    return True

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    
    v = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        v[a].append(b)
        v[b].append(a)
    
    visited = [-1 for _ in range(n + 1)]
    
    flag = True
    for i in range(1, n + 1):
        if visited[i] != -1:
            continue
            
        flag = bfs(i)
        
        if not flag:
            break
            
    if flag:
        print('YES')
    
    else:
        print('NO')