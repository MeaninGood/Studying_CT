import sys
input = sys.stdin.readline

sys.setrecursionlimit(50010)

def dfs(cur, prv):
    par[cur] = prv
    for nxt in v[cur]:
        if nxt == prv:
            continue
        
        dfs(nxt, cur)

n = int(input())
v = [[] for _ in range(n + 1)]

par = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    
    v[a].append(b)
    v[b].append(a)
    

dfs(1, 0)

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    
    a = []
    while x != 0:
        a.append(x)
        x = par[x]
        
    b = []
    while y != 0:
        b.append(y)
        y = par[y]

    idx1 = len(a) - 1
    idx2 = len(b) - 1
    
    while idx1 >= 0 and idx2 >= 0 and a[idx1] == b[idx2]:
        idx1 -= 1
        idx2 -= 1 
        
    print(a[idx1 + 1])