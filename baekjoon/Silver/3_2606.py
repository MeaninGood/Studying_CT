visited = [False for i in range(110)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)


n = int(input())
m = int(input())

v = [[] for i in range(110)]
for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)
    
dfs(1)

print(visited.count(True) - 1)