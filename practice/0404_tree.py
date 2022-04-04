# 부모 노드 찾기

n = int(input())
v = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)
par = [0 for i in range(n + 1)]

def dfs(cur, prv):
    par[cur] = prv
    
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        dfs(nxt, cur)
        
dfs(1, -1)

for i in range(2, n + 1):
    print(par[i])
    
    
    

# 서브 트리 // 각 서브트리의 크기 구하기
n, r, q = map(int, input().split())
v = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)

sz = [0 for i in range(n + 1)]

def dfs(cur, prv):
    sz[cur] = 1
    
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        sz[cur] += dfs(nxt, cur)
        
    return sz[cur]

dfs(r, -1)

for i in range(q):
    x = int(input())
    
    print(sz[x])
    


# 가장 가까운 공통 조상
