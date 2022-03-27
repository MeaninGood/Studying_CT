import sys
from collections import deque
si = sys.stdin.readline


def bfs(s):
    que = deque()
    visited = [False for i in range(200010)]
    cnt = 0
    ret = 0
    
    que.append(s)
    visited[s] = True
    
    while len(que) > 0:
        size = len(que)

        for _ in range(size):
            cur = que.popleft()
            
            if cur == k:
                ret += 1
     
            for nxt in [cur -1, cur + 1, 2 * cur]:
                if not (0 <= nxt < 200010) or visited[nxt]:
                    continue
                
                visited[nxt] = True
                que.append(nxt)
                
        cnt += 1
    # visited[cur] = False
    return cnt, ret

n, k = map(int, si().split())

v = [i for i in range(200010)]


print(bfs(n))
        
