import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def get_dist(x, y, d):
    pq = []
    
    heapq.heappush(pq, [d, x, y])
    dist[x][y] = d
    while pq:
        d, x, y = heapq.heappop(pq)
        
        if x == n - 1 and y == m - 1:
            return d
        
        if dist[x][y] != d:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not in_range(nx, ny):
                continue
            
            nd = d + arr[nx][ny]
            
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, [nd, nx, ny])
            


m, n = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dist = [[10000000 for i in range(m)] for j in range(n)]

print(get_dist(0, 0, 0))