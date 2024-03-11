import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(k + 1)] for _ in range(n)]


def recur(cur, w):
    if w > k:
        return -1 << 31

    if cur == n:
        return 0

    if dp[cur][w] != -1:
        return dp[cur][w]

    dp[cur][w] = max(recur(cur + 1, w + arr[cur][0]) + arr[cur][1], recur(cur + 1, w))

    return dp[cur][w]


print(recur(0, 0))
