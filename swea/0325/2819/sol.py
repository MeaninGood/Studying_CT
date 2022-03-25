# import sys
# si = sys.stdin.readline

# def in_range(x, y):
#     return 0 <= x < 4 and 0 <= y < 4

# visited = [[False for _ in range(4)] for _ in range(4)]
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def dfs(x, y):
#     cnt = 1
    
#     if cnt == 7:
#         return 1
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
        
#         if not in_range(nx, ny):
#             continue
        
#         cnt += 1
#         dfs(nx, ny)
#     dp[x][y] = 

# v = [list(map(int, si().split())) for _ in range(4)]

# total = 0
# for i in range(4):
#     for j in range(4):
#         total += dfs(i, j)