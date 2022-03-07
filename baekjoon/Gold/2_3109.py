# 3109번_빵집

## 빵집이 있는 곳은 R*C 격자로 표현
## 첫째 열은 근처 빵집의 가스관이고, 마지막 열은 원웅이의 빵집
## 가스관과 빵집을 연결하는 파이프를 설치
## 빵집과 가스관 사이에는 건물이 있을 수 있고, 파이프를 놓을 수 없다.
## 모든 파이프라인은 첫째 열에서 시작해야 하고, 마지막 열에서 끝남
## 각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결, 각 칸의 중심끼리 연결
## 설치할 수 있는 가스관과 빵집을 연결하는 파이프라인의 최대 개수 구하기


'''
# 첫째 줄에 R과 C가 주어진다. (1 ≤ R ≤ 10,000, 5 ≤ C ≤ 500)
# 다음 R개 줄에는 빵집 근처의 모습이 주어짐
# '.'는 빈 칸이고, 'x'는 건물
# 처음과 마지막 열은 항상 비어있음
## 첫째 줄에 원웅이가 놓을 수 있는 파이프라인의 최대 개수를 출력

(입력)
3 4
DLLL
DRLU
RRRU

(출력)
2

'''

import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
# x는 0에서 시작, 끝에서 끝나야 함
dx = [-1, 0, 1]
dy = [1, 1, 1]

visited = [[False for i in range(m)] for j in range(n)]


def dfs(x, y):
    global ans
    visited[x][y] = True

    if y == m - 1 :
        ans += 1
        return True
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 'x' or visited[nx][ny]:
            continue
        
        if dfs(nx, ny):
            return True
        
    return False
           
    
ans = 0 
for i in range(n):
    if arr[i][0] == '.' and not visited[i][0]:
       dfs(i, 0)

print(ans)