di = [-1, -1]
dj = [-1, 1]

def check(x, y):
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


n_queen(0)
print(global_cnt)