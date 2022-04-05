from collections import deque

def in_range(x):
    return 0 <= x < 1000100

def bfs(s):
    que = deque()
    visited = [False for i in range(1000100)]
    
    que.append(s)
    visited[s] = True
    
    ret = 0
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            if cur == m:
                return ret
            
            for nxt in [cur + 1, cur - 1, cur * 2, cur - 10]:
                if not in_range(nxt) or visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
        
        ret += 1
    
T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    print(f'#{tc} {bfs(n)}')