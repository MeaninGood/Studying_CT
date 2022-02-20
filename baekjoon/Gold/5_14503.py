n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while 1:
    arr[x][y] = 2 # 청소한다
    
    moved = False # 이동 했나 안 했나 판단
    for i in range(4): # 4방향 둘러보기
        d = (d + 3) % 4 # 좌회전 (d+3)%4, 우회전 (d+1)%4
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        # 0이면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
            
            moved = True # 이동을 했다
            break
        
    if not moved: # moved가 False면
        nx = x + dx[(d + 2) % 4] # 뒤쪽 방향 보기 == x - dx[d]
        ny = y + dy[(d + 2) % 4] # 뒤쪽 방향 보기 == y - dy[d]
        
        if arr[nx][ny] == 2:
            x = nx
            y = ny
        
        else:
            break
        
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 :
            cnt += 1
            
print(cnt)