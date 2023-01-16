# # # import sys, heapq
# # # from pprint import pprint
# # # from collections import deque
# # # input = lambda : sys.stdin.readline().strip()


# # # def in_range(x, y):
# # #     return 0 <= x < n + 2 and 0 <= y < m + 2

# # # # 0: 홀수, 1: 짝수
# # # dx = [[-1, 0, 0, 1, 1, 1], [-1, -1, -1, 0, 0, 1]]
# # # dy = [[0, -1, 1, -1, 0, 1], [-1, 0, 1, -1, 1, 0]]
# # # # def get_dist(x, y, d, cnt):
# # # #     pq = []
# # # #     dist[x][y] = d

# # # #     heapq.heappush(pq, [d, x, y, cnt])
# # # #     while pq:
# # # #         d, x, y, cnt = heapq.heappop(pq)

# # # #         if cnt == 4:
# # # #             return d

# # # #         if dist[x][y] != d:
# # # #             continue

# # # #         for i in range(6):
# # # #             if x % 2 == 1:
# # # #                 nx = x + dx[0][i]
# # # #                 ny = y + dy[0][i]

# # # #             else:
# # # #                 nx = x + dx[1][i]
# # # #                 ny = y + dy[1][i]

# # # #                 if not in_range(nx, ny):
# # # #                     continue

# # # #                 nd = d + arr[nx][ny]

# # # #                 if dist[nx][ny] > nd:
# # # #                     dist[nx][ny] = d
# # # #                     heapq.heappush(pq, [nd, nx, ny, cnt + 1])
    
# # # def bfs(x, y, cnt):
# # #     que = deque()
# # #     visited = [[False for i in range(m + 2)] for j in range(n + 2)]

# # #     que.append([x, y, 1])
# # #     visited[x][y] = True

# # #     while que:
# # #         size = len(que)

# # #         for _ in range(size):
# # #             x, y, cnt = que.popleft()

# # #             for d in range(6):
# # #                 if x % 2 == 1:



# # # m, n = map(int, input().split())
# # # arr = [[0 for i in range(m + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]\
# # #     + [[0 for i in range(m + 2)]]

# # # # dist = [[1 << 31 for i in range(m + 2)] for j in range(n + 2)]

# # # # get_dist(0, 0, 0, 0)
# # # pprint(arr)
# # # print('====================')
# # # # pprint(dist)


# # # """
# # # 5 3
# # # 100 200 300 200 100
# # # 300 200 100 200 300
# # # 100 100 100 100 100

# # # """


# # import sys, heapq
# # from pprint import pprint
# # from collections import deque
# # input = lambda : sys.stdin.readline().strip()

# # def in_range(x, y):
# #     return 0 <= x < n + 2 and 0 <= y < n + 2

# # def get_range(x, y):
# #     return 1 <= x < n + 1 and 1 <= y < n + 1

# # dx = [0, 1, 0, -1]
# # dy = [1, 0, -1, 0]
# # def get_dist(x, y, d, i):
# #     pq = []
# #     dist[x][y] = arr[x][y]

# #     heapq.heappush(pq, [d, x, y])
# #     while pq:
# #         d, x, y = heapq.heappop(pq)

# #         if dist[x][y] != d:
# #             continue

# #         nx = x + dx[i]
# #         ny = y + dy[i]

# #         if not in_range(nx, ny):
# #             continue

# #         if arr[nx][ny] == 100:
# #             continue

# #         nd = d + arr[nx][ny]

# #         if dist[nx][ny] > nd:
# #             if dist[nx][ny] == INF:
# #                 dist[nx][ny] = nd
# #             else:
# #                 dist[nx][ny] = max(dist[nx][ny], nd)

# #             heapq.heappush(pq, [nd, nx, ny])

# # n = int(input())
# # arr = [[0 for i in range(n + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]\
# #     + [[0 for i in range(n + 2)]]

# # for i in range(1, n + 1):
# #     for j in range(1, n + 1):
# #         if arr[i][j] == 1:
# #             arr[i][j] = 100

# #         if arr[i][j] == 0:
# #             arr[i][j] = 1

# # INF = 1 << 31
# # dist = [[INF for i in range(n + 2)] for j in range(n + 2)]

# # get_dist(0, 0, 0, 0)
# # get_dist(0, n + 1, 0, 1)
# # get_dist(n + 1, 0, 0, 2)
# # get_dist(n + 1, n + 1, 0, 3)
# # pprint(arr)
# # print('====================')
# # pprint(dist)

# # """"
# # [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# #  [0, 1, 1, #, 1, 1, 1, 1, 0],
# #  [0, 1, 2, #, 2, 2, 2, 1, 0],
# #  [0, 1, 2, 3, 3, 3, #, 1, 0],
# #  [0, 1, 2, 3, 4, 3, 2, 1, 0],
# #  [0, #, #, 3, #, 3, 2, 1, 0],
# #  [0, 1, #, 2, 2, 2, 2, 1, 0],
# #  [0, 1, 1, 1, 1, 1, 1, 1, 0],
# #  [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# # [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# #  [0, 1, 1, #, 1, 1, 1, 1, 0],
# #  [0, 1, 2, #, 2, 2, 2, 1, 0],
# #  [0, 1, 2, 3, 3, 3, #, 1, 0],
# #  [0, 1, 2, 3, 4, 3, 2, 1, 0],
# #  [0, #, #, 3, #, 3, 2, 1, 0],
# #  [0, 1, #, 2, 2, 2, 2, 1, 0],
# #  [0, 1, 1, 1, 1, 1, 1, 1, 0],
# #  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# # """



# import sys, heapq
# from pprint import pprint
# from collections import deque
# input = lambda : sys.stdin.readline().strip()


# def in_range(x, y):
#     return 0 <= x < n + 2 and 0 <= y < n + 2

# n = int(input())
# arr = [[0 for i in range(n + 2)]] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)]\
#     + [[0 for i in range(n + 2)]]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if arr[i][j] == 1:
#             arr[i][j] = '#'

#         if arr[i][j] == 0:
#             arr[i][j] = 1

# dist1 = [[0 for i in range(n + 2)] for j in range(n + 2)]
# # 왼 -> 오
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if arr[i][j] == '#':
#             dist1[i][j] = '!'
#             break
#         dist1[i][j] = dist1[i][j - 1] + 1
# for i in range(1, n + 1):
#     if n in dist1[i]:
#         dist1[i] = [0 for i in range(n + 2)]

# # 오 -> 왼
# for i in range(1, n + 1):
#     for j in range(1, n + 1)[::-1]:
#         if arr[i][j] == '#':
#             dist1[i][j] = '!'
#             break
        
#         if dist1[i][j] != 0:
#             dist1[i][j] = min(dist1[i][j], dist1[i][j + 1] + 1)
#         else:
#             dist1[i][j] = dist1[i][j + 1] + 1

# for i in range(1, n + 1):
#     if n in dist1[i]:
#         dist1[i] = [0 for i in range(n + 2)]

# # 위 -> 밑
# dist2 = [[0 for i in range(n + 2)] for j in range(n + 2)]
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if arr[j][i] == '#':
#             dist2[j][i] = '!'
#             break
#         dist2[j][i] = dist2[j - 1][i] + 1

#         if dist2[j][i] == n:
#             for k in range(1, n + 1):
#                 dist2[k][i] = 0

# # 밑 -> 위
# for i in range(1, n + 1):
#     for j in range(1, n + 1)[::-1]:
#         if arr[j][i] == '#':
#             dist2[j][i] = '!'
#             break
        
#         if dist2[j][i] != 0:
#             dist2[j][i] = min(dist2[j][i], dist2[j + 1][i] + 1)
#         else:
#             dist2[j][i] = dist2[j + 1][i] + 1

#         if dist2[j][i] == n:
#             for k in range(1, n + 1)[::-1]:
#                 dist2[k][i] = 0


# pprint(arr)
# pprint(dist1)
# pprint(dist2)

# """
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 2, '!', 4, 3, 2, 1, 0],
#  [0, 1, 2, '!', 4, 3, 2, 1, 0],
#  [0, 1, 2, 3, 4, 5, '!', 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, '!', 0, 0, '!', 3, 2, 1, 0],
#  [0, 1, '!', 5, 4, 3, 2, 1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 1, 1, '!', 1, 0, 1, 0, 0],
#  [0, 2, 2, '!', 2, 0, 2, 0, 0],
#  [0, 3, 3, 5, 3, 0, '!', 0, 0],
#  [0, 4, 4, 4, 4, 0, 4, 0, 0],
#  [0, '!', '!', 3, '!', 0, 3, 0, 0],
#  [0, 2, '!', 2, 2, 0, 2, 0, 0],
#  [0, 1, 1, 1, 1, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# """

# visited = [[False for i in range(n + 2)] for j in range(n + 2)]
# for i in range(2, n - 1):
#     if '!' in dist1[i]:
#         for j in range(2, n - 1):
#             visited[i] = True
            
# pprint(visited)   













# import sys, heapq
# from pprint import pprint
# from collections import deque
# input = lambda : sys.stdin.readline().strip()



# def in_range(x, y):
#     return 0 <= x < 33 and 0 <= y < 33

# ddx = [0, 1, 0, -1]
# ddy = [1, 0, -1, 0]
# # def get_dist(x, y, d):
# #     pq = []
# #     dist[x][y] = d

# #     heapq.heappush(pq, [d, x, y])
# #     ret = 0
# #     while pq:
# #         d, x, y = heapq.heappop(pq)

# #         if dist[x][y] != d:
# #             continue
        
# #         for i in range(4):
# #             nx = x + ddx[i]
# #             ny = y + ddy[i]

# #             if not in_range(nx, ny) or arr[nx][ny] == -1:
# #                 continue

# #             if arr[nx][ny] == '#':
# #                 return True

# #             nd = d + arr[nx][ny]
# #             if dist[nx][ny] > nd:
# #                 dist[nx][ny] = nd

# #                 heapq.heappush(pq, [nd, nx, ny])

# #         ret += 1
# def bfs(x, y):
#     que = deque()
    
#     que.append([x, y])
#     visited[x][y] = True

#     ret = 0
#     while que:
#         size = len(que)

#         for _ in range(size):
#             x, y = que.popleft()

#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]

#                 if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] != 1:
#                     continue

#                 que.append([nx, ny])
#                 visited[nx][ny] = True

# dx = [-1, -1, -1, 0, 0, 1, 1, 1]
# dy = [-1, 0, 1, -1, 1, -1, 0, 1]
# arr = [[-1 for i in range(33)] for j in range(33)]
# dist = [[1 << 31 for i in range(33)] for j in range(33)]
# houses = []
# n = int(input())
# for k in range(n):
#     x, y, cnt = map(int, input().split())
#     x, y = 16 + x, 16 + y
#     houses.append([x, y])
#     arr[x][y] = '#'
#     dist[x][y] = 0

#     tmpx, tmpy = x, y
#     for d in range(8):
#         if d in [0, 2, 5, 7]:
#             total = cnt // 2

#         else:
#             total = cnt

#         idx = 0
#         while idx != total:
#             nx = tmpx + dx[d]
#             ny = tmpy + dy[d]
#             if not (0 <= nx < 33 and 0 <= ny < 33):
#                 break

#             arr[nx][ny] = 1
#             tmpx, tmpy = nx, ny
#             idx += 1

#         tmpx, tmpy = x, y

# visited = [[False for i in range(33)] for j in range(33)]

# cnt = 1
# for i in range(33):
#     for j in range(33):
#         if arr[i][j] == '#':
#             if get_dist(x, y, 0):
#                 visited[i][j] = True
#                 cnt += 1
# mx = 0
# ans = 99999999
# if cnt == n:
#     # for i in range(33):
#     #     for j in range(33):
#     #         if dist[i][j] != 1 << 31:
#     #             mx = max(dist[i][j], mx)

#     # for i in range(33):
#     #     for j in range(33):
#     #         if mx == dist[i][j]:
#     #             tmp = 0
#     #             for k in range(n):
#     #                 tmp += abs(houses[k][0] - i) + abs(houses[k][1] - j)
#     #                 print(houses[k][0], i, houses[k][1], j, tmp)

#     #             ans = min(tmp, ans)

#     for i in range(33):
#         for j in range(33):
#             if visited[i][j]:
#                 tmp = 0
#                 for k in range(n):
#                     tmp += abs(houses[k][0] - i) + abs(houses[k][1] - j)
#                     print(houses[k][0], i, houses[k][1], j, tmp)
                
#                 ans = min(tmp, ans)

#     print(ans)
# else:
#     print(-1)


            
            



# # print(arr)
# # print(dist)

# """

# """


import sys, heapq
from pprint import pprint
from collections import deque
input = lambda : sys.stdin.readline().strip()

def in_range(x, y):
    return 0 <= x < 33 and 0 <= y < 33

ddx = [0, 1, 0, -1]
ddy = [1, 0, -1, 0]
def bfs(x, y):
    global double
    que = deque()
    
    que.append([x, y])
    visited[x][y] = True
    while que:
        size = len(que)

        for _ in range(size):
            x, y = que.popleft()

            if arr[x][y] == '#':
                check[x][y] = True

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if not in_range(nx, ny) or arr[nx][ny] != 1:
                    continue

                if visited[nx][ny]:
                    double.add((nx, ny))
                    continue

                que.append([nx, ny])
                visited[nx][ny] = True

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
arr = [[-1 for i in range(33)] for j in range(33)]

houses = []
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    for k in range(n):
        x, y, cnt = map(int, input().split())
        x, y = 16 + x, 16 + y
        houses.append([x, y])
        arr[x][y] = '#'
        print(arr[x][y])
        tmpx, tmpy = x, y
        for d in range(8):
            if d in [0, 2, 5, 7]:
                total = cnt // 2

            else:
                total = cnt

            idx = 0
            while idx != total:
                nx = tmpx + dx[d]
                ny = tmpy + dy[d]
                if not (0 <= nx < 33 and 0 <= ny < 33) or arr[nx][ny] == '#':
                    break

                arr[nx][ny] = 1
                tmpx, tmpy = nx, ny
                idx += 1

            tmpx, tmpy = x, y

    visited = [[False for i in range(33)] for j in range(33)]
    check = [[False for i in range(33)] for j in range(33)]
    double = set()
    cnt = 1
    for i in range(33):
        for j in range(33):
            if arr[i][j] == '#' and not check[i][j]:
                bfs(i, j)

    aa = 0
    for i in range(33):
        for j in range(33):
            if check[i][j]:
                aa += 1
    mx = 0
    ans = 99999999
    if aa == n:
        for i in range(33):
            for j in range(33):
                if visited[i][j]:
                    tmp = 0
                    for k in range(n):
                        tmp += abs(houses[k][0] - i) + abs(houses[k][1] - j)
                        print(houses[k][0], i, houses[k][1], j, tmp)
                    
                    ans = min(tmp, ans)

        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {-1}')

print(cnt, aa)
print(arr)
print(double)
double.add((0, 0))


"""
"""