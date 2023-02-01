import sys
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# ㅡ V
# dx1 = [0, 0, 0, 0]
# dy1 = [0, 1, 2, 3]

# ㅣ V
# dx2 = [0, 1, 2, 3]
# dy2 = [0, 0, 0, 0]
#

# ㅁ V
# yellow_dx = [0, 0, 1, 1]
# yello_dy = [0, 1, 0, 1]

# # L - 1번 V
# orange_dx1 = [0, 1, 2, 2]
# orange_dy1 = [0, 0, 0, 1]

# # 2번
# orange_dx2 = [0, 0, 1, 2]
# orange_dx2 = [0, 1, 0, 0]

# L 대칭 - 4방향

# Z - 4방향

# Z 대칭 - 4방향

# ㅜ 4방향

# 범위 초과하면 return 0, 아니면 return 합



dx = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 0, 1, 1], # ㅡ ㅣ ㅁ
      
      [0, 1, 1, 1], [0, 0, 1, 2], [0, 0, 0, 1], [0, 1, 2, 2], # L
      [0, 0, 0, 1], [0, 0, 1, 2], [1, 1, 1, 0], [0, 1, 2, 2], # L 대칭
      [0, 1, 1, 2], [1, 1, 0, 0], [0, 1, 1, 2], [0, 0, 1, 1], # Z , Z 대칭
      [1, 0, 1, 1], [0, 1, 1, 2], [0, 0, 0, 1], [1, 0, 1, 2]] # ㅗ

dy = [[0, 1, 2, 3], [0, 0, 0, 0], [0, 1, 0, 1], # 다 맞음....
      
      [0, 0, 1, 2], [0, 1, 0, 0], [0, 1, 2, 2], [1, 1, 1, 0], #
      [0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 2, 2], [0, 0, 0, 1],
      [0, 0, 1, 1], [0, 1, 1, 2], [1, 1, 0, 0], [0, 1, 1, 2],
      [0, 1, 1, 2], [0, 0, 1, 0], [0, 1, 1, 2], [0, 1, 1, 1]]
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