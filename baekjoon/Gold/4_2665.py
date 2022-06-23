import sys, heapq
input = sys.stdin.readline


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def get_dist(x, y, arr):
    pq = []
    dist[x][y] = arr[x][y]
    
    heapq.heappush(pq, (arr[x][y], x, y))
    
    while pq:
        d, x, y = heapq.heappop(pq)
        
        if x == n - 1 and y == n - 1:
            return d
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not in_range(nx, ny):
                continue
            
            nd = dist[x][y] + arr[nx][ny]
            
            if dist[nx][ny] > nd:
                dist[nx][ny] = nd
                heapq.heappush(pq, (nd, nx, ny))
                
            

    

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr[i][j] = 0
            
        else:
            arr[i][j] = 1

dist = [[1000000000 for _ in range(n)] for _ in range(n)]

print(get_dist(0, 0, arr))