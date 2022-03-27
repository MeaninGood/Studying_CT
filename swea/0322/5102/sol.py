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

