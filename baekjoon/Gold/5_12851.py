import sys
from collections import deque
input = sys.stdin.readline

cnt = 1
def bfs(s):
    global cnt
    
    que = deque()
    visited = [False for i in range(100010)]
    
    que.append(s)
    visited[s] = True
    ret = 0
    while len(que) > 0:
        size = len(que)

        for _ in range(size):
            cur = que.popleft()
            
            visited[cur] = True
            
            if cur == k:
                for i in que:
                    print(i)
                    if i == k:
                        cnt += 1        
                return ret
     
            for nxt in [cur -1, cur + 1, 2 * cur]:
                if not (0 <= nxt < 100010) or visited[nxt]:
                    continue

                que.append(nxt)
                
        ret += 1
        print(f'#{ret}')

n, k = map(int, input().split())

print(bfs(n))
print(cnt)

