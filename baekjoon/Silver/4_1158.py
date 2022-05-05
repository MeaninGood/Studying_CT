n, m = map(int, input().split())
arr = [i + 1 for i in range(n)]
visited = [False for i in range(n)]

ans = []
i = 0
s = 0
while len(ans) < n:
    if visited[i % n]:
        i += 1
        continue
    
    elif s == m - 1:
        ans.append(arr[i % n])
        visited[i % n] = True
        s = 0
        continue
    
    i += 1
    s += 1
    
print('<', end = '')
print(*ans, sep = ', ', end = '')
print('>')