# 1726번_로봇

## 명령 1. Go k: k는 1, 2 또는 3. 현재 향하고 있는 방향으로 k칸 만큼 움직임.
## 명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전
## 0은 로봇이 갈 수 있는 지점, 1은 로봇이 갈 수 없는 지점
## 로봇의 현재 위치와 바라보는 방향이 주어졌을 때
## 로봇을 원하는 위치로 이동시키고, 원하는 방향으로 바라보도록 하는데 최소 몇 번의 명령이 필요한지 구하는 프로그램

'''
# 첫째 줄에 직사각형의 세로 길이 M과 가로 길이 N이 빈칸을 사이에 두고 주어짐
# 이때 M과 N은 둘 다 100이하의 자연수
# 이어 M줄에 걸쳐 한 줄에 N개씩 숫자 0 또는 1이 빈칸을 사이에 두고 주어짐
# 다음 줄에는 로봇의 출발 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어짐
# 마지막 줄에는 로봇의 도착 지점의 위치 (행과 열의 번호)와 바라보는 방향이 빈칸을 사이에 두고 주어짐
# 방향은 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
# 출발지점에서 도착지점까지는 항상 이동이 가능
## 첫째 줄에 로봇을 도착 지점에 원하는 방향으로 이동시키는데 필요한 최소 명령 횟수를 출력

(입력)
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 1

(출력)
9

'''

from collections import deque

n, m = map(int, input().split())
v = [[0 for _ in range(m + 1)]] + [[0] + list(map(int, input().split())) for j in range(n)]
sx, sy, sd = map(int, input().split())
ex, ey, ed = map(int, input().split())

# 북동남서 0 1 2 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
change_dir = [0, 1, 3, 2, 0]

def in_range(x, y):
    return 0 <= x < n + 1 and 0 <= y < m + 1

def bfs(x, y, dir):
    que = deque()
    visited = [[[False for _ in range(4)] for i in range(n + 1)] for j in range(m + 1)]
    ret = 0
    
    que.append([x, y, dir])
    visited[x][y][dir] = True
    
    cnt = 0
    moved = False
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y, dir = que[0][0], que[0][1], que[0][2]
            que.popleft()
            
            if x == ex and y == ey and dir == ed:
                return ret
             
            for i in range(4):
                    
                if moved == False and dir == 2 or dir == 3:
                    d = change_dir[d]
                
                    nx = x + dx[i]
                    ny = y + dy[i]
                    dir = (d + 1) % 4

                if not in_range or visited[nx][ny] or v[nx][ny] != 0:
                    moved = False # 이동 했나 안 했나 판단   
                    ret += 1
                    continue
                # 이거 아닌 것 같다고 ㅠ
                elif moved and cnt <= 3:
                    que.append([nx, ny, dir])
                    visited[nx][ny][dir] = True
                    cnt += 1
                # 아 이거 움직이는 거 while문으로 cnt 3전까지 돌려야 ㅎ는디 어케 해 ㅠ?
                
                # 이걸 다음 사이즈에서 해줘야 하는데 왜 같은 사이즈에서 하고 있냐고
                moved = True
                que.append([nx, ny, dir])
                visited[nx][ny][dir] = True
                cnt += 1 
            
                if cnt > 3:
                    cnt = 0
                    continue
    
    return ret

print(bfs(sx, sy, sd))


# from collections import deque
#
# n, m = map(int, input().split())
# arr = [input() for i in range(n)]
# visited = [[[False for k in range(3)] for i in range(m)] for j in range(n)]
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# que = deque()
#
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < m
#
# d = 1

# que.append([0, 0, 0])
# visited[0][0][0] = True
# while len(que) > 0:
#     size = len(que)
#
#     for _ in range(size):
#         x, y, hand = que[0][0], que[0][1], que[0][2]
#         que.popleft()
#
#         if x == n - 1 and y == m - 1:
#             print(d)
#             exit()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if not in_range(nx, ny):
#                 continue
#
#             nhand = hand + int(arr[nx][ny])
#
#             if nhand > 1 or visited[nx][ny][nhand]:
#                 continue
#
#             que.append([nx, ny, nhand])
#             visited[nx][ny][nhand] = True
#
#     d += 1
#
# print(-1)