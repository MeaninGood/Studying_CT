dx = [-1, -1]
dy = [-1, 1]

def in_range(x, y):
    return 0 <= x and 0 <= y < n

def check(x, y):
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
            
        if not in_range(nx, ny):
            continue
        
        if arr[nx][ny]:
            return False
            
    return True


def n_queen(cnt):
    global global_cnt
    
    if cnt == n:
        global_cnt += 1
        
    for i in range(n):
        if not visited[i] and check(cnt, i):
            arr[cnt][i] = 1
            visited[i] = True
            n_queen(cnt + 1)
            arr[cnt][i] = 0
            visited[i] = False
    return

n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]

global_cnt = 0

n_queen(0)
# result = n_queen(0)
print(global_cnt)

di = [-1, -1]
dj = [-1, 1]

def check(x, y):
    # 현재 위치에서 왼쪽 위, 오른쪽 위에 퀸이 있는지 확인
    for j in range(2):
        nx, ny = x, y
        while True:
            nx += di[j]
            ny += dj[j]
            if nx < 0 or ny >= N or ny < 0:
                break
            if arr[nx][ny]:
                return False
    return True


def n_queen(cnt):
    global global_cnt
    if cnt == N:
        global_cnt += 1
        return
    for i in range(N):
        if visited[i] == 0 and check(cnt, i):
            arr[cnt][i] = 1
            visited[i] = 1
            n_queen(cnt + 1)
            arr[cnt][i] = 0
            visited[i] = 0
    return



N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]
global_cnt = 0


result = n_queen(0)
print(global_cnt)