# 5x5 배열 


arr = [list(map(int, input().split())) for i in range(5)]


for i in range(5):
    for j in range(5) :
        if arr[i][j] < arr[i]
        
        
dx = [1, 0, -1, 0]  
dy = [0, 1, 0, -1]
dir = 0

for i in range(n * n + 1):
    arr[x][y] == i
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if not (0 <= nx < n and 0 <= ny  < n) and arr[x][y] != 0:
        dir = (dir + 1) % 4
        
    x += dx[dir]
    y += dy[dir]