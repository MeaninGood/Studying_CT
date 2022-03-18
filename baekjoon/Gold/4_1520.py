# 1520번_내리막길

## 제일 왼쪽 위 칸에서 제일 오른쪽 아래 칸으로 이동
## 항상 높이가 더 낮은 지점으로만 이동
## 경로의 개수를 구하기

'''
# 첫째 줄에는 지도의 세로 M과 가로 N이 빈칸을 사이에 두고 주어짐
# M개 줄에 걸쳐 한 줄에 N개씩 각 지점의 높이가 빈 칸을 사이에 두고 주어짐
# M과 N은 각각 500이하의 자연수이고, 각 지점의 높이는 10000이하의 자연수
## 첫째 줄에 이동 가능한 경로의 수 H를 출력
## 모든 입력에 대하여 H는 10억 이하의 음이 아닌 정수


(입력)
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

(출력) 
3

'''



# m, n = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(m)]

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# dp = [[-1 for i in range(n)] for j in range(m)]
    
# def recur(x, y):
#     ret = 0
   
#     if x == m - 1 and y == n - 1:
#         return 1
    
#     if dp[x][y] != -1:
#         return dp[x][y]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if not (0 <= nx < m and 0 <= ny < n) or arr[nx][ny] >= arr[x][y]:
#             continue
        
#         ret += recur(nx, ny)
    
#     dp[x][y] = ret
    
#     return ret
# print(recur(0, 0))












dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    ret = 0
    
    if x == n - 1 and y == m - 1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if not in_range(nx, ny) or v[nx][ny] >= v[x][y]:
            continue
        
        ret += dfs(nx, ny)
        
    dp[x][y] = ret
    return ret

n, m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for i in range(m)] for j in range(n)]

print(dfs(0, 0))
