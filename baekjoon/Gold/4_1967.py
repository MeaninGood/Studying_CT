import sys
input = sys.stdin.readline
sys.setrecursionlimit(10010)


def dfs(cur, prv, total):
    global mx, idx
    
    if mx < total:
        mx = total
        idx = cur
        
    for nxt, d in v[cur]:
        if nxt == prv:
            continue
        
        dfs(nxt, cur, total + d)



n = int(input())
v = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    
    v[a].append([b, c])
    v[b].append([a, c])
    
    
idx = 0
mx = 0
dfs(1, -1, 0)
dfs(idx, -1, 0)
print(mx)
