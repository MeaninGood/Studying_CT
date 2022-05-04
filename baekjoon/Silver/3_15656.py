m, n = map(int, input().split())

arr = sorted(list(map(int, input().split())))

v = [0 for i in range(n)]
# visited = [False for i in range(m + 1)]

def recur(cur):
    if cur == n:
        print(*v)
        return
    
    for i in range(m):
        # if visited[i]:
        #     continue
        
        v[cur] = arr[i]
        # visited[i] = True
        recur(cur + 1)
        # visited[i] = False
        
recur(0)