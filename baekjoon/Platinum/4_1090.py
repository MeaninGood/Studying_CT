import sys
from pprint import pprint
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# x좌표, y좌표 뽑기
xs, ys = set(), set()
for x, y in arr:
    xs.add(x)
    ys.add(y)
    
# 가능한 좌표
new_arr = set()
for i in xs:
    for j in ys:
        new_arr.add((i, j))

# 좌표 간의 거리 누적합 배열 구하기
dist = []
for a, b in new_arr:
    tmp_arr = []
    for x, y in arr:
        total = abs(a - x) + abs(b - y)
        tmp_arr.append(total)
        
    tmp_arr.sort()
    for k in range(1, n):
        tmp_arr[k] = tmp_arr[k] + tmp_arr[k - 1]
        
    dist.append(tmp_arr)
        
# 최소거리 좌표 뽑기
ans = [1 << 31 for _ in range(n)]
for i in range(n):
    for j in range(len(dist)):
        ans[i] = min(dist[j][i], ans[i])
        
print(*ans)