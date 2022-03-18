from collections import deque

def bfs(s):
    que = deque()
    visited = [False for _ in range(n + 1)]

    
    que.append(s)
    visited[s] = True
    d = 0
    
    while len(que) > 0:
        ans = []
        size = len(que)
        
        for _ in range(size):
            cur = que.popleft()
            
            ans.append(cur)
            
            for nxt in v[cur]:
                if not (0 <= nxt < n + 1) or visited[nxt]:
                    continue
                
                que.append(nxt)
                visited[nxt] = True
        
        d += 1

    return ans

for tc in range(1, 11): 
    n, s = map(int, input().split())
    v = [[] for _ in range(n + 1)]
    arr = list(map(int, input().split()))

    for i in range(0, len(arr) - 1, 2):
        v[arr[i]].append(arr[i + 1])

    


    print(f'#{tc} {max(bfs(s))}')
    

'''
1 17 
3 22 
1 8 
1 7 
7 1 
2 7 
2 15 
15 4 
6 2 
11 6 
4 10 
4 2

'''