import sys
sys.setrecursionlimit(100000)

def dfs(cur):
    visited[cur] = True
    
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)


n, m = map(int, sys.stdin.readline().split())

arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    arr[b].append(a)
    
ans = []
mx = 0
for i in range(n+1):
    visited = [False for _ in range(n+1)]
    dfs(i)
    ans.append(visited.count(True))
    mx = max(mx, ans[i-1])

print(ans)
for i in range(n+1):
    if ans[i] == mx:
        print(i, end = ' ')




'''
6 8
1 5
1 6
2 5
2 1
3 5
4 2
5 1
6 2
'''