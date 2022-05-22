from collections import deque

def in_range(x, y):
    return 0 <= x < n + 1 and 0 <= y < m + 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    global d
    que = deque()
    visited = [[False for i in range(m + 1)] for j in range(n + 1)]
    
    que.append([x, y])
    visited[x][y] = True
    
    ret = 0
    while que:
        size = len(que)
        
        for _ in range(size):
            x, y = que.popleft()
            
            if (arr[x][y] in d) and (d[arr[x][y]] == False):
                d[arr[x][y]] = True
                return ret
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == '#':
                    continue
                
                que.append([nx, ny])
                visited[nx][ny] = True
                
        ret += 1
        
    return -1

visit = [False, False, False]
tmp = [[], [], []]

def recur(cur):
    global idx
    if cur == 3:
        idx.append(tmp)
        return
    
    for i in range(3):
        if visit[i]:
            continue
        
        tmp[i] = a[i]
        visit[i] = True
        recur(cur + 1)
        visit[i] = False

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [['#' for _ in range(m + 1)]] + [(['#'] + list(input())) for _ in range(n)]

    d = {'B': False, 'C': False, '_': False}
    a = [list(map(int, input().split())) for _ in range(3)]
    idx = []
    
    recur(0)

    ans = 100000000
    for i in range(6):
        flag = False
        dist = 0
        for j in range(3):
            x, y = idx[i][j]
            
            tmp2 = bfs(x, y)
            
            if tmp2 == -1:
                flag = True
            
            dist += tmp2

        if not flag:    
            ans = min(ans, dist)
        
    if ans == 100000000:
        print(f'#{tc} -1')
    
    else:
        print(f'#{tc} {ans}')