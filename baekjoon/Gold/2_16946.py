# 16946번_벽 부수고 이동하기 4

## N×M의 행렬로 표현되는 맵
## 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽
## 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸
## 1. 벽을 부수고 이동할 수 있는 곳으로 변경
## 2. 그 위치에서 이동할 수 있는 칸의 개수를 세어보기


'''
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
# 다음 N개의 줄에 M개의 숫자로 맵이 주어짐
## 맵의 형태로 정답을 출력
## 원래 빈 칸인 곳은 0을 출력
## 벽인 곳은 이동할 수 있는 칸의 개수를 10으로 나눈 나머지를 출력

(입력)
3 3
101
010
101

(출력)
303
050
303

'''

# import sys
# from collections import deque
# input = sys.stdin.readline


# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def bfs(x, y, hand):
#     que = deque()
    
#     que.append([x, y, hand])
#     visited[x][y][hand] = True
    
#     while que:
#         size = len(que)
        
#         for _ in range(size):
#             x, y, hand = que.popleft()
            
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
                
#                 if not in_range(nx, ny):
#                     continue
                
#                 nhand = hand + arr[nx][ny]
                
#                 if nhand > 1 or visited[nx][ny][nhand]:
#                     continue
                
#                 ans[nx][ny] += 1
                
#                 que.append([nx, ny, nhand])
#                 visited[nx][ny][nhand] = True
                

# n, m = map(int, input().split())
# arr = [list(map(int, input().rstrip())) for _ in range(m)]

# visited = [[[False, False] for i in range(m)] for j in range(n)]
# ans = [[0 for i in range(m)] for j in range(n)]

# for i in range(n):
#     for j in range(m):
#         for k in range(2):
#             if visited[i][j][k] or arr[i][j] == 0:
#                 continue
            
#             bfs(i, j, k)
# print(ans)



import sys
from collections import deque
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    que = deque()
    visited = [[False for i in range(m)] for j in range(n)]
    
    # if dp[x][y] != -1:
    #     return dp[x][y]
    
    que.append([x, y])
    visited[x][y] = True
    
    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            ret += 1
            
            # if dp[x][y] != -1:
            #     return dp[x][y]
             
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != 0:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
        # dp[x][y] = ret
    return ret
                

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[-1 for i in range(m)] for j in range(n)]


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = bfs(i, j)
    
for i in arr:
    print(*i, sep='')


# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# n, m = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# visited = [[False for i in range(m)] for j in range(n)]

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# # visited = [[False for i in range(m)] for j in range(n)]
# dp = [[-1 for i in range(m)] for j in range(n)]

# def dfs(x, y):
#     if dp[x][y] != -1:
#         return dp[x][y]
    
#     visited[x][y] = True
    
#     ret = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0 or visited[nx][ny]:
#             continue

#         ret += dfs(nx, ny)
#     visited[x][y] = False
#     dp[x][y] = ret
#     return ret

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 1:
#             arr[i][j] = dfs(i, j)
# for i in arr:
#     print(*i, sep='')
