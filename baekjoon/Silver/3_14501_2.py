import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ret = -1


def recur(cur, total):
    global ret

    if cur > n:
        return

    if cur == n:
        ret = max(total, ret)
        return

    x, y = arr[cur]
    recur(cur + x, total + y)
    recur(cur + 1, total)


recur(0, 0)

print(ret)
