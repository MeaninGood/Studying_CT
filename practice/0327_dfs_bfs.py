# 1260 DFS와 BFS

# from collections import deque
# import sys
# sys.setrecursionlimit(100000)

# def dfs(cur):
#     visited[cur] = True
    
#     print(cur, end = ' ')
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         dfs(nxt)
        

# def bfs(s):
#     que = deque()
#     li = [False for _ in range(n + 1)]
    
#     que.append(s)
#     li[s] = True
    
#     while len(que) > 0 :
#         size = len(que)
        
#         for _ in range(size):
#             cur = que.popleft()
            
#             print(cur, end = ' ')
            
#             for nxt in v[cur]:
#                 if li[nxt]:
#                     continue
                
#                 que.append(nxt)
#                 li[nxt] = True


# n, m, k = map(int, input().split())
# v = [[] for _ in range(n + 1)]

# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)

# for i in v:
#     i.sort()

# visited = [False for _ in range(n + 1)]

# dfs(k)
# print()
# bfs(k)




# 2606 바이러스

# import sys
# sys.setrecursionlimit(100)

# def dfs(cur):
#     ret = 1
#     visited[cur] = True
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         ret += dfs(nxt)
    
#     return ret
        

# n = int(input())
# m = int(input())
# v = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    
# visited = [False for _ in range(n + 1)]
# print(dfs(1) - 1)




# 2644 촌수계산

# from collections import deque

# def bfs(s):
#     que = deque()
#     visited = [False for _ in range(n + 1)]

#     que.append(s)
#     visited[s] = True
    
#     ret = 0
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             cur = que.popleft()
            
#             if cur == e:
#                 return ret
            
#             for nxt in v[cur]:
#                 if visited[nxt]:
#                     continue
                
#                 que.append(nxt)
#                 visited[nxt] = True
        
#         ret += 1
    
#     return -1
                
            


# n = int(input())
# s, e = map(int, input().split())
# m = int(input())
# v = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    
# print(bfs(s))




# 11724 연결 요소의 개수

# def dfs(cur):
#     visited[cur] = True
    
#     for nxt in v[cur]:
#         if visited[nxt]:
#             continue
        
#         dfs(nxt)



# n, m = map(int, input().split())
# v = [[] for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)
    
# visited = [False for _ in range(n + 1)]

# cnt = 0
# for i in range(1, n + 1):
#     if not visited[i]:
#         dfs(i)
#         cnt += 1
        
# print(cnt)
    




# 16562 친구비

# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
# v = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
    
#     v[a].append(b)
#     v[b].append(a)



dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
    # for i in [(0, 1), (1, 0), (0, -1), (-1,0)]:
        if not (0 <= nx < n - 1 and 0 <= ny < m - 1) or v[nx][ny] == 0 or visited[nx][ny]:
            continue
        
        dfs(nx, ny)

from collections import deque    
def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]

    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0 :
        x, y = que[0][0], que[0][1]
        que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n - 1 and 0 <= ny < m - 1) or v[nx][ny] == 0 or visited[nx][ny]:
                continue
            
            que.append([nx, ny])
            visited[nx][ny] = True            
            
    
    
n, m = map(int, input())
v = [list(map(int, input())) for _ in range(n)]

visited = [[False for i in range(m)] for j in range(n)]