# 1926번_그림

## 어떤 큰 도화지에 그림이 그려져 있을 때
## 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
## 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의
## 가로나 세로는 연결 된 것, 대각선으로 연결이 된 것은 떨어진 그림
## 그림의 넓이란 그림에 포함된 1의 개수

'''
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)
# 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어짐
# 단 그림의 정보는 0과 1이 공백을 두고 주어지며,
# 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미
## 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력
## 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0

(입력)
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

(출력)
4
9

'''

import sys
sys.setrecursionlimit(100000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    ret = 1
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 0 or visited[nx][ny]:
            continue
        
        ret += dfs(nx, ny)
    return ret
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt += 1
            ans = max(ans, dfs(i, j))
            
if cnt == 0:
    print(cnt, 0, sep='\n')
else:
    print(cnt, ans, sep='\n')
    
'''
6 5
0 0 1 0 0
0 0 0 0 0
0 1 0 0 0
1 0 0 0 1 
0 1 0 0 0
1 1 1 0 0

'''