import sys

sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [-1 for _ in range(n)]


def recur(cur):
    if cur > n:
        return -1 << 31

    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))

    return dp[cur]


print(recur(0))
