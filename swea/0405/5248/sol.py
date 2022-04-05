def dfs(cur):
    visited[cur] = True
    
    for nxt in v[cur]:
        if visited[nxt]:
            continue
        
        dfs(nxt)

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    v = [[] for i in range(n + 1)]
    li = list(map(int, input().split()))
    for i in range(0, m * 2 - 1, 2):
        v[li[i]].append(li[i + 1])
        v[li[i + 1]].append(li[i])

    visited = [False for i in range(n + 1)]

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
            
    print(f'#{tc} {cnt}')

