# 2583번_영역 구하기

## 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이
## 눈금에 맞추어 K개의 직사각형을 그릴 때,
## 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나뉨
## 분리된 영역 개수와 각 영역의 넓이가 얼마인지를 구하여 이를 출력

'''
# 첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 주어짐
# M, N, K는 모두 100 이하의 자연수
# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 
# 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어짐
# 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)
# 오른쪽 위 꼭짓점의 좌표는(N,M)
# 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다
## 첫째 줄에 분리되어 나누어지는 영역의 개수를 출력
## 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력

(입력)
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

(출력)
3
1 7 13

'''


# import sys
# sys.setrecursionlimit(100000)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# def dfs(x, y):
#     ret = 1
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny] !=0 or visited[nx][ny]:
#             continue
        
#         ret += dfs(nx, ny)
#     return ret

# m, n, k = map(int, input().split())
# arr = [[0]*n for _ in range(m)]

# for _ in range(k):
#     y1, x1, y2, x2 = map(int, input().split())
    
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             arr[i][j] = 1
            
# visited = [[False]*n for _ in range(m)]
# cnt = 0
# li = []
# for i in range(m):
#     for j in range(n):
#         if arr[i][j] == 0 and not visited[i][j]:
#             cnt += 1
#             li.append(dfs(i, j))

# li.sort()
# print(cnt)
# print(*li)




### bfs로 다시 풀기!

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    que = deque()
    ret = 1
    
    que.append([x, y])
    visited[x][y] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            x, y = que[0][0], que[0][1]
            que.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if not in_range(nx, ny) or visited[nx][ny] or v[nx][ny] != 0:
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
                ret += 1
        
    return ret                  
    
    
n, m, k = map(int, input().split())
v = [[0 for i in range(m)] for _ in range(n)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            v[i][j] = 1
            
visited = [[False for i in range(m)] for j in range(n)]

cnt = 0
ans = []
for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and not visited[i][j]:
            cnt += 1
            ans.append(bfs(i, j))
          
ans.sort()       
print(cnt)
print(*ans)