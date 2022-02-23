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

