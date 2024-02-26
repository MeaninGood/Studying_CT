import sys

input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10010)


def recur(cur, total, cnt):
    global ret
    if cur == n:
        if total == m and cnt > 0:
            ret += 1
        return

    recur(cur + 1, total + arr[cur], cnt + 1)
    recur(cur + 1, total, cnt)


n, m = map(int, input().split())
arr = list(map(int, input().split()))

ret = 0
recur(0, 0, 0)
print(ret)
