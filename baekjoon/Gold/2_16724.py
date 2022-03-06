# 16724번_피리 부는 사나이

## U, D, L, R이고 각각 위, 아래, 왼쪽, 오른쪽으로 이동
## 설정해 놓은 방향을 분석해서 최소 개수의 ‘SAFE ZONE’을 만들기
## 지도 어느 구역에 있더라도 ‘SAFE ZONE’에 들어갈 수 있게 하는
## ‘SAFE ZONE’의 최소 개수를 출력

'''
# 첫 번째 줄에 지도의 행의 수를 나타내는 N(1 ≤ N ≤ 1,000)
# 지도의 열의 수를 나타내는 M(1 ≤ M ≤ 1,000)
# 두 번째 줄부터 N개의 줄에 지도의 정보를 나타내는 길이가 M인 문자열이 주어짐
# 지도 밖으로 나가는 방향의 입력은 주어지지 않음
## 첫 번째 줄에 ‘SAFE ZONE’의 최소 개수를 출력

(입력)
3 4
DLLL
DRLU
RRRU

(출력)
2

'''

import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 'DRUL'

def dfs(x, y):
    global cnt
    visited[x][y] = True
    
    nx = x + dx[d.index(arr[x][y])]
    ny = y + dy[d.index(arr[x][y])]
    
    if safe[nx][ny]:
        cnt -= 1
        safe[x][y] = True
        return 

    if visited[nx][ny]:
        safe[x][y] = True
        return

    dfs(nx, ny)
    safe[x][y] = True
    
    
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

    
visited = [[False for i in range(m)] for j in range(n)]
safe = [[False for i in range(m)] for j in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j)
            
print(cnt)