# 23563번_벽 타기

## 높이가 H이고 너비가 W인 맵에서 시작점 -> 끝점 이동
##  각 칸은 벽 또는 빈칸
## 벽으로는 이동할 수 없으며, 한 칸을 이동하는 데 1초
## 벽을 타고(벽에 인접한 칸으로) 이동하면 0초
## 시작점에서 끝점까지 이동하는 데 걸리는 최소 시간 구하기

'''
# 첫째 줄에 H와 W가 공백을 사이에 두고 주어짐
# 둘째 줄부터, H개의 줄에 걸쳐서 맵의 모습을 나타내는 W개의 문자가 주어짐
# #은 벽, .은 빈칸, S는 맵의 시작점, E는 맵의 끝점
## 맵의 시작점에서 끝점까지 이동하는 데 걸리는 최소 시간을 출력

(입력)
10 10
##########
#........#
#...#....#
#........#
#.E....S.#
#........#
#........#
##.......#
#........#
##########

0000000000
0000000000
0011011100
00......00
00E....S00
00......00
00......00
000.....00
0000000000
0000000000

(출력)
2

'''

# import sys
# import heapq
# from pprint import pprint
# si = sys.stdin.readline

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m

# # cx = [-1, -1, -1, 0, 0, 1, 1, 1]
# # cy = [-1, 0, 1, -1, 1, -1, 0, 1]
# cx = [0, 1, 0, -1]
# cy = [1, 0, -1, 0]
# def walls(x, y):
#     for c in range(4):
#         wx = x + cx[c]
#         wy = y + cy[c]
        
#         # if not in_range(wx, wy) or arr[wx][wy] == '#':
#         #     continue
        
#         # arr[wx][wy] = 0
#         if not in_range(wx, wy):
#             continue
        
#         if arr[wx][wy] == '#':
#             return True
        
#     return False
            
            
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def get_dist(x, y, arr):
#     pq = []
#     dist[x][y] = 0
    
#     heapq.heappush(pq, (0, x, y))
#     while len(pq) > 0:
#         d, x, y = heapq.heappop(pq)
        
#         if dist[x][y] != d:
#             continue
        
#         # if x == ex and y == ey:
#         #     return
        
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             if not in_range(nx, ny):
#                 continue
            
#             if arr[nx][ny] == '#':
#                 continue
            
#             # if arr[nx][ny] == '.' or arr[nx][ny]and not walls(nx, ny):
#             #     nd = dist[x][y] + 1
            
#             # if not walls(nx, ny):
#             #     nd = dist[x][y] + 1
            
#             # if arr[nx][ny] == '.' and walls(nx, ny):
#             #     nd = dist[x][y] + 0
                
#             if walls(x, y) and walls(nx, ny):
#                 nd = dist[x][y] + 0
            
#             else:
#                 nd = dist[x][y] + 1
                

#             if dist[nx][ny] > nd:
#                 dist[nx][ny] = nd
#                 heapq.heappush(pq, (nd, nx, ny))
            
    


# n, m = map(int, si().split())
# arr = [list(si().rstrip()) for _ in range(n)]
# sx, sy = 0, 0
# ex, ey = 0, 0
# for i in range(n):
#     for j in range(m):
#         # if arr[i][j] == '.':
#         #     arr[i][j] = 1
#         if arr[i][j] == 'S':
#             sx, sy = i, j
#             # arr[i][j] = 1
#         if arr[i][j] == 'E':
#             ex, ey = i, j
#             # arr[i][j] = 1


# # for i in range(n):
# #     for j in range(m):
# #         if arr[i][j] == '#':
# #             walls(i, j)

# # pprint(arr)
            
# # print(arr, sx, sy, ex, ey)
# dist = [[1000000000 for i in range(m)] for j in range(n)]

# get_dist(sx, sy, arr)
# # print(dist)
# print(dist[ex][ey])




import sys, heapq
si = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

cx = [0, 1, 0, -1]
cy = [1, 0, -1, 0]
def walls(x, y):
    for c in range(4):
        wx = x + cx[c]
        wy = y + cy[c]

        if not in_range(wx, wy):
            continue
        
        if arr[wx][wy] == '#':
            return True
        
    return False
            
            
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def get_dist(x, y, arr):
    pq = []
    dist[x][y] = 0
    
    heapq.heappush(pq, (0, x, y))
    while len(pq) > 0:
        d, x, y = heapq.heappop(pq)
        
        if dist[x][y] != d:
            continue
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not in_range(nx, ny):
                continue
            
            if arr[nx][ny] == '#':
                continue
                
            if walls(x, y) and walls(nx, ny):
                nd = dist[x][y] + 0
            
            else:
                nd = dist[x][y] + 1
                

            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, (nd, nx, ny))
            
    


n, m = map(int, si().split())
arr = [list(si().rstrip()) for _ in range(n)]
sx, sy = 0, 0
ex, ey = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            sx, sy = i, j

        if arr[i][j] == 'E':
            ex, ey = i, j


dist = [[1000000000 for i in range(m)] for j in range(n)]

get_dist(sx, sy, arr)

print(dist[ex][ey])