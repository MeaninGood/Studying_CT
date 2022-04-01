import sys
from collections import deque
sys.setrecursionlimit(10000)

def dfs(cur):
    visited[cur] = True
    
    print(cur, end = ' ')
    
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)

def bfs(s):
    que = deque()
    visit = [False for i in range(len(arr))]
    
    que.append(s)
    visit[s] = True
    
    while len(que) > 0:
        size = len(que)
        
        for i in range(size):
            cur = que.popleft()
            
            print(cur, end = ' ')
            
            for nxt in arr[cur]:
                if visit[nxt]:
                    continue
                
                que.append(nxt)
                visit[nxt] = True     
    


tmp = list(map(int, input().split()))
arr = [[] for i in range(max(tmp) + 1)]
for i in range(0, len(tmp), 2):
    arr[tmp[i]].append(tmp[i + 1])
    # arr[tmp[i + 1]].append(tmp[i])
    
visited = [False for i in range(len(arr))]
print(arr)
dfs(1)
print()
bfs(1)