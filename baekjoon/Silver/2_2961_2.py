import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 1 << 31


def recur(cur, stotal, btotal, cnt):
    global res

    if cur == n:
        if cnt > 0:
            res = min(res, abs(stotal - btotal))
        return

    recur(cur + 1, stotal * arr[cur][0], btotal + arr[cur][1], cnt + 1)
    recur(cur + 1, stotal, btotal, cnt)


recur(0, 1, 0, 0)
print(res)
