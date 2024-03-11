import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [0 for _ in range(m)]


def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        arr[cur] = i
        recur(cur + 1)
        arr[cur] = 0


recur(0)
