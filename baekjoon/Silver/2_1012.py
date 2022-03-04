# 1012번_유기농 배추

## 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅
## 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사

'''
# 첫 줄에는 테스트 케이스의 개수 T
# 각 T별 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50)
# 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어짐
# 두 배추의 위치가 같은 경우는 없음
## 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력

(입력)
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

(출력)
5
1

'''

import sys
sys.setrecursionlimit(100000)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y):
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or arr[nx][ny] != 1:
            continue
        
        dfs(nx, ny)


T = int(sys.stdin.readline())
for tc in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    arr = [[0]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        arr[x][y] = 1
        

    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    print(cnt)

# love you