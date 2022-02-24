n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [ 0 for i in range(n)]
visited = [False for i in range(n)]


def recur(cur):
    cnt = 0
    if cur == n:
        total = 0
        for i in range(n):
            total += arr[arr2[i]]
            return total
            
        if total == s:
            cnt += 1
        return cnt
    
    for i in range(n):
        if visited[i]:
            continue
        
        arr2[cur] = i
        visited[i] = True
        cnt += recur( cur + 1 )
        visited[i] = False
    
    return cnt

print(recur(0))