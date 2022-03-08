import sys
sys.setrecursionlimit(100000)

li = []

def dfs(cur):
    ret = 1
    visited[cur] = True
    li.append(cur)
    
    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        
        ret += dfs(nxt)
    return ret


n, m = map(int, sys.stdin.readline().split())

arr = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    
    arr[b].append(a)
    
visited = [False for i in range(n + 1)]
ans = []
mx = 0
for i in range(n+1):
    a = dfs(i)
    ans.append(a)
    mx = max(mx, a)
    
    for i in li:
        visited[i] = False
    li.clear()
        

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