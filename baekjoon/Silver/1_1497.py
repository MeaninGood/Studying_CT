import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [list(input().split()) for _ in range(n)]

res = 1 << 31
tmp = ["N" for _ in range(m)]


def recur(cur, cnt):
    if cur == n:
        if "N" not in tmp:
            res = min(res, cnt)
        return

    # 고른다
    for i in range(m):
        if arr[cur][i] == "Y":
            tmp[i] = arr[cur][i]
            recur(cur + 1, cnt + 1)
    # 안 고른다
    recur(cur + 1, cnt)
