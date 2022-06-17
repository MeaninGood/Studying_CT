import sys
from collections import deque
input = sys.stdin.readline


def bfs(cur):
    que = deque()
    
    que.append(cur)
    visited[cur] = True
    
    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            if cur == k:
                return ret
            
            for nxt in [cur - 1, cur + 1, 2 * cur]:
                if not (0 <= nxt < 100010) or visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                prv[nxt] = cur
                
        ret += 1
    
n, k = map(int, input().split())
visited = [False for _ in range(100010)]
prv = [-1 for _ in range(100010)]

print(bfs(n))

idx = k
ans = []
while idx != -1:
    ans.append(idx)
    idx = prv[idx]
    
print(*ans[::-1])