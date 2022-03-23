1.
# 6 6 17
# 5 4 6
# 5 2 5
# 0 4 2
# 2 3 3
# 1 2 7
# 0 1 3
# => 1 2 3
# 4 2 10
# 0 1 2
# 0 2 3
# => 0 1
# 4 4 11
# 0 1 2
# 1 2 7
# 2 3 10
# 3 0 9
# => -1
import sys
si = sys.stdin.readline
N, M, K = map(int, si().split())
con = [[] for _ in range(N)]
for _ in range(M):
    x, y, c = map(int, si().split())
    con[x].append((y, c))
    con[y].append((x, c))
dp = [[False for _ in range(K + 1)] for _ in range(N)]
dp[0][0] = True
for dist in range(1, K + 1):  # => O(K)
    # 이중 포문 다 합치면 O(M)
    for i in range(N):
        # 지금 풀고 싶은 문제: dp[i][dist]
        for j, c in con[i]:
            if dist - c >= 0:
                # dp[i][dist] = dp[i][dist] or dp[j][dist - c]
                # 위와 같은 코드
                dp[i][dist] |= dp[j][dist - c]
                
flag = False
for i in range(N):
    if dp[i][K]:
        print(i, end=' ')
        flag = True
if not flag:
    print(-1)