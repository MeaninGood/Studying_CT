import sys
input = sys.stdin.readline

def dfs(cur, prv):
    global ans
    
    cnt = 0
    for nxt in v[cur]:
        if nxt == m:
            continue
            
        dfs(nxt, cur)
        cnt += 1
        
    if cnt == 0:
        ans += 1
    
    
n = int(input())
par = list(map(int, input().split()))
m = int(input())
v = [[] for _ in range(n)]

idx = 0
for i in range(n):
    if par[i] == -1:
        idx = i
    
    else:    
        v[par[i]].append(i)

ans = 0
dfs(idx, -2)
print(ans if m != idx else 0)