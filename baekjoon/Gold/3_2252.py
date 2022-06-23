import sys
input = sys.stdin.readline

sys.setrecursionlimit(32010)

def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)

    st.append(cur)
    
n, m = map(int, input().split())
v = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
st = []


for _ in range(m):
    a, b = map(int, input().split())
    v[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
    
print(*st)
