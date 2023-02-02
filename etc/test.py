import sys
from collections import deque
input= sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

N,M,K = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]


def bfs ():

    q= deque()
    q.append((0,0,0,0)) # 0 낮 1 밤
    dist =[[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    dist[0][0] = 1
    visited[0][0] = 1

    while q:
        x,y,z,time = q.popleft()
            
        if x == M-1 and y == N-1:
            return dist[N-1][M-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny <N:
                #  벽 x 이동
                if graph[ny][nx] ==0 and dist[ny][nx] == 0 and visited[ny][nx] ==0:
                    if visited[y][x] == 1:
                        dist[ny][nx] = dist[y][x] + 1
                        visited[ny][nx] += 1
                    elif visited[y][x] == 2:
                        dist[ny][nx] = dist[y][x]
                        visited[ny][nx] += 1
                    q.append((nx,ny,z,(time+1)%2))
                # 낮 벽 부수고 이동
                elif graph[ny][nx]== 1 and time == 0 and z<=K and dist[ny][nx] ==0 and visited[ny][nx] ==0:
                    if visited[y][x] <= 2:
                        dist[ny][nx] =dist[y][x] + 1
                        visited[ny][nx] += 1
                    elif visited[y][x] > 2:
                        dist[ny][nx] =dist[y][x]
                        visited[ny][nx] += 1
                    q.append((nx,ny,z+1,(time+1)%2))
                # 밤 이동 x
                elif graph[ny][nx]== 1  and time == 1:
                    if visited[y][x] == 1:
                        dist[y][x] =dist[y][x] + 1
                        visited[y][x] += 1
                    elif visited[y][x] == 2:
                        visited[y][x] += 1
                        continue
                    q.append((x,y,z,(time+1)%2))
                        
    return -1

print(bfs())