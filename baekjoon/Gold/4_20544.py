import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
ret = 0

# 0, 1, 2
dp = [[-1 for _ in range(4)] for _ in range(n)]


# 현재, 높이, 이전 높이
def recur(cur, h, prv):
    global ret

    if cur == n:
        return 1

    if dp[cur][h] != -1:
        return dp[cur][h]

    for i in range(3):
        if prv + i >= 4:
            continue

        dp[cur][h] = recur(cur + 1, h + i, i)

    return dp[cur][h]


print(recur(0, 0, 0))
