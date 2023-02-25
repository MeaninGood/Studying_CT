import sys
<<<<<<< HEAD
import copy
from pprint import pprint
input = lambda : sys.stdin.readline().strip()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, dir, sec, arr):
    global visited
    arr.append([x, y])
    for i in range(l):
        a, b = dirs[i]

        for j in range(1, a + 1):
            nx = x + (dx[dir] * j)
            ny = y + (dy[dir] * j)
            print("nx = x + dx[dir] * j:", nx, x, dx[dir] * j, "ny = y + dy[dir] * j: ", ny, y, dy[dir] * j, "nx, ny = ", nx, ny)

            if not in_range(nx, ny) or visited[nx][ny] or [nx, ny] in arr:
                return sec

            if [nx, ny] in apples:
                arr.append([nx, ny])
                sec += 1
            
            elif [nx, ny] not in apples:
                arr.pop(0)
                arr.append([nx, ny])
                sec += 1

        for vx, vy in arr:
            visited[vx][vy] = True

        if b == 'D':
            dir = (dir - 1) % 4

        elif b == 'L':
            dir = (dir + 1) % 4
        
        dfs(nx, ny, dir, sec, [])

n = int(input())
k = int(input())
apples = []
for i in range(k):
    a, b = map(int, input().split())
    apples.append([a - 1, b - 1])
l = int(input())
tmp_dir = []
for i in range(l):
    a, b = input().split()
    tmp_dir.append([int(a), b])

dirs = copy.deepcopy(tmp_dir)
for i in range(1, l):
    dirs[i][0] = tmp_dir[i][0] - tmp_dir[i - 1][0]


visited = [[False for i in range(n)] for j in range(n)]
print(dfs(0, 0, 1, 0, []))
pprint(visited)
=======
input = lambda : sys.stdin.readline().strip()


n = int(input())
arr = [list(input()) for _ in range(n)]

d = {}
for i in range(n):
    idx = len(arr[i])
    for j in range(len(arr[i])):
        tmp = 10 ** (idx - 1) # 가중치 부여 (자릿수)
        if d.get(arr[i][j]):
            d[arr[i][j]] += tmp
        
        else:
            d[arr[i][j]] = d.get(arr[i][j], tmp)
        
        idx -= 1
        
li = sorted(d.items(), key=lambda x : -x[1]) # value 기준으로 정렬

total = 0
idx = 9
for k, v in li:
    total += idx * v # 10000의 자리 A에 9를 넣는다는 것 = 9가 10000개 있다는 뜻이므로 total에 바로 곱해서 더하기
    idx -= 1
    
print(total)
>>>>>>> bb75b48a28c0dd0a593604a0a5a3b60bdd2935de
