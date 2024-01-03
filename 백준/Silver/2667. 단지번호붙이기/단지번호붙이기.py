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