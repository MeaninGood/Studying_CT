# 4963번_섬의 개수

## 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램 작성
## 한 정사각형과 가로, 세로 또는 대각선으로 연결

'''
# 입력은 여러 개의 테스트 케이스
# 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h
# w와 h는 50보다 작거나 같은 양의 정수
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다
# 입력의 마지막 줄에는 0이 두 개
## 각 테스트 케이스에 대해서, 섬의 개수를 출력

(입력)
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

(출력)
0
1
1
3
1
9

'''

import sys

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(x, y):
    visited[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < m and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] != 1:
            continue
        
        dfs(nx, ny)
    

while True:
    n, m = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    if n == 0 and m == 0:
        break
    
    visited = [[False]*n for _ in range(m)]
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    print(cnt)                