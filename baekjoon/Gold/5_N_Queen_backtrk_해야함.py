n = int(input())
arr = [ 0 for i in range(n)]
visited = [False for i in range(n)]

def check(cur):
    

def recur(cur):
    if cur == n:
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        arr[cur] = i
        visited[i] = True
        recur( cur + 1)
        visited[i] = False