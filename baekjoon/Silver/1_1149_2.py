import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(3)] for _ in range(n)]


def recur(cur, prv):
    if cur == n:
        return 0

    if dp[cur][prv] != -1:
        return dp[cur][prv]

    ret = 1 << 31
    for i in range(3):
        if i == prv:
            continue

        ret = min(recur(cur + 1, i) + arr[cur][i], ret)

    dp[cur][prv] = ret
    return ret


print(recur(0, -1))
