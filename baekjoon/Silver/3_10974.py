def recur(cur):
    if cur == n:
        print(*v)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        v[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False
        
n = int(input())
v = [0 for i in range(n)]
visited = [False for i in range(n + 1)]
recur(0)