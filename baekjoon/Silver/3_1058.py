import sys
input = lambda : sys.stdin.readline().strip()


def dfs(cur):
    visited[cur] = True
    
    ret = 1
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        ret += dfs(nxt)
        visited[nxt] = False
    
    return ret        
    

n = int(input())
arr = [list(input()) for _ in range(n)]

v = [[] for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'Y':
            v[i + 1].append(j + 1)
            v[j + 1].append(i + 1)
            

ans = -10000000 
for i in v:
    ans = max(ans, len(i))

print(v)
print(ans)


visited = [False for _ in range(n + 1)]
for i in range(1, n + 1):
    if not visited[i]:
        print(dfs(i))
        