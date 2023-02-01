import sys
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 0, 1, 1], # ㅡ ㅣ ㅁ
      [0, 1, 1, 1], [0, 0, 1, 2], [0, 0, 0, 1], [0, 1, 2, 2], # L
      [0, 0, 0, 1], [0, 0, 1, 2], [1, 1, 1, 0], [0, 1, 2, 2], # L 대칭
      [0, 1, 1, 2], [1, 1, 0, 0], [0, 1, 1, 2], [0, 0, 1, 1], # Z , Z 대칭
      [0, 1, 1, 1], [0, 1, 1, 2], [0, 0, 0, 1], [1, 0, 1, 2]] # ㅗ

dy = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 1, 0, 1], # 다 맞음....
      [0, 0, 1, 2], [0, 1, 0, 0], [0, 1, 2, 2], [1, 1, 1, 0], # 다 맞는데...
      [0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 0, 0, 1], # 다 맞음...
      [0, 0, 1, 1], [0, 1, 1, 2], [1, 1, 0, 0], [0, 1, 1, 2], # 맞음..
      [1, 0, 1, 2], [0, 0, 1, 0], [0, 1, 2, 1], [0, 1, 1, 1]]

def tet(x, y):
    ret = -1000000
    for i in range(19):
        total = 0
        for j in range(4):
            nx = x + dx[i][j]
            ny = y + dy[i][j]
            
            if not in_range(nx, ny):
                total = 0
                break
            
            total += arr[nx][ny]
            
        ret = max(ret, total)
            
    return ret

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = -100000
for i in range(n):
    for j in range(m):
        answer = max(answer, tet(i, j))
        
print(answer)