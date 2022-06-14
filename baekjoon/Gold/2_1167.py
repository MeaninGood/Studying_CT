import sys
input = sys.stdin.readline


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
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[] for _ in range(n + 1)]

for i in range(n):
    for j in range(1, len(arr[i]), 2):
        if arr[i][j] == -1:
            break
        
        a = j
        b = j + 1
        v[arr[i][0]].append([arr[i][a], arr[i][b]])
       
idx = 0
mx = 0
dfs(1, -1, 0)
dfs(idx, mx, 0)

print(mx)