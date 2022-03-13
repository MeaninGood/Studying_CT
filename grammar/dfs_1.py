# 1. 연결 요소의 크기 구하는 함수

# def dfs(cur):
#     ret = 1
#     visited[cur] = True

#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue

#         ret += dfs(nxt) # 각 노드당 ret +1 씩 돼서 더해짐

#     return ret

# n = int(input())
# m = int(input())
# v = [[] for i in range(n + 1)]

# for i in range(m):
#     a, b = map(int, input().split())

#     v[a].append(b)
#     v[b].append(a)

# visited = [False for i in range(n + 1)]

# print(dfs(1))




# 2. 연결 요소 개수 구하기

# def dfs(cur):
#     visited[cur] = True
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         dfs(nxt) 

# n, m = map(int, input().split())
# v = [[] for i in range(n + 1)]

# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    

# visited = [False for i in range(n + 1)]

# cnt = 0
# for i in range(1, n + 1):
#     if visited[i]:
#         continue
    
#     dfs(i)
#     cnt += 1
    
# print(cnt)



# 3. 플러드필 (육지 1, 바다 0)

# < 2667 >
# def dfs(cur):
#     visited[cur] = True
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         dfs(nxt)

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
   
# def dfs(x, y):
#     ret = 1
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if not ( 0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] == '0':
#             continue
        
#         ret += dfs(nx, ny)
    
#     return ret
    

# n = int(input())
# arr = [ input() for i in range(n) ]

# visited = [[False for i in range(n)] for j in range(n)]
# cnt = 0
# ans = []
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] or arr[i][j] == '0':
#             continue
        
#         cnt += 1
#         ans.append(dfs(i, j))
        
# print(cnt) # cnt 안 쓸 거면 len(ans)
# ans.sort()
# for i in ans:
#     print(i)
    
    

# 10026

import sys
sys.setrecursionlimit(10010)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or v[x][y] != v[nx][ny]:
            continue
        
        dfs(nx, ny)

n = int(input())
v = [input() for i in range(n)]

visited = [[False for i in range(n)] for i in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        
        cnt += 1
        dfs(i, j)
        
print(cnt, end = ' ')


for i in range(n):
    p = ''
    for j in range(n):
        if v[i][j] == 'G':
            p += 'R'
        else:
            p += v[i][j]
    v[i] = p

ans = 0
visited = [[False for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        
        ans +=1
        dfs(i, j)
print(ans)
