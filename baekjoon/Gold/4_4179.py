import sys
from collections import deque
import copy
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 지훈이
def jihun_bfs(x, y, d):
    que = deque()
    
    que.append([d, x, y])
    visited[x][y] = 0
    road[d] = road.get(d, 0) + 1

    ret = n * n
    while que:
        d, x, y = que.popleft()

        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            ret = min(ret, d + 1)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) or visited[nx][ny] == 'F' or visited[nx][ny] == '#':
                continue
            
            if visited[nx][ny] == '.':
                nd = d + 1
                visited[nx][ny] = nd
                road[nd] = road.get(nd, 0) + 1
                que.append([nd, nx, ny])

    return ret


def fire_bfs(x, y, d):
    global road
    que = deque()
    
    que.append([d, x, y])
    li[x][y] = 'F'
    while que:
        d, x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) or li[nx][ny] == '#' or li[nx][ny] == 'F':
                continue

            if li[nx][ny] == d:
                if road[nd] < 0:
                    return False

            nd = d + 1
            li[nx][ny] = 'F'
            road[nd] = road.get(nd, 0) - 1
            que.append([nd, nx, ny])

    return True


jihun = [0, 0]
fires = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'J':
            jihun = [i, j]

        if arr[i][j] == 'F':
            fires.append([i, j])

visited = copy.deepcopy(arr)
road = {}
tmp = jihun_bfs(jihun[0], jihun[1], 0)
print(road)

li = copy.deepcopy(visited)

flag = False
for i in range(len(fires)):
    flag = fire_bfs(fires[i][0], fires[i][1], 1)
    if not flag:
        print('IMPOSSIBLE')
        print(road)
        exit()



# print(arr)
# print(visited)
# print(li)
print(tmp)