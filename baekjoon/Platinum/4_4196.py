import sys
input = sys.stdin.readline

sys.setrecursionlimit(10010)
def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)
        
    st.append(cur)

def dfs2(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs2(nxt)


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    
    v = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    st = []
    for _ in range(m):
        a, b = map(int, input().split())
        v[a].append(b)
        
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    
    visited = [False for _  in range(n + 1)]
    cnt = 0
    while len(st) > 0:
        if not visited[st[-1]]:
            dfs2(st[-1])
            cnt += 1
            
        st.pop()
        
    print(cnt)