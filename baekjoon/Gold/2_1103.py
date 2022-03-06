# 1103번_게임

## 1부터 9까지의 숫자와, 구멍이 있는 직사각형 보드
## 보드의 가장 왼쪽 위에 동전은 다음과 같이 움직임.
## 1. 동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
## 2. 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
## 3. 동전을 위에서 고른 방향으로 X만큼 움직인다. 이때, 중간에 있는 구멍은 무시한다.
## 만약 동전이 구멍에 빠지거나, 보드의 바깥으로 나간다면 게임은 종료
## 최대 몇 번 동전을 움직일 수 있는지 구하는 프로그램

'''
# 첫째줄에 보드의 세로 크기 N과 가로 크기 M, 모두 50보다 작거나 같은 자연수
# 둘째 줄부터 N개의 줄에 보드의 상태가 주어짐
# 쓰여 있는 숫자는 1부터 9까지의 자연수 또는 H
# 가장 왼쪽 위칸은 H가 아니고, H는 구멍
## 첫째 줄에 문제의 정답을 출력
## 만약 형택이가 동전을 무한번 움직일 수 있다면 -1을 출력

(입력)
3 7
3942178
1234567
9123532

(출력)
5

'''

import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[False for i in range(m)] for j in range(n)]
def dfs(x, y):
    visited[x][y] = True
    
    ret = 1
    for i in range(4):
        nx = x + (dx[i] * int(arr[x][y]))
        ny = y + (dy[i] * int(arr[x][y]))
        
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 'H':
            continue
        
        if visited[nx][ny]:
            print(-1)
            exit()
        
        ret = max(ret, dfs(nx, ny) + 1)
    visited[x][y] = False
    return ret

print(dfs(0, 0))

