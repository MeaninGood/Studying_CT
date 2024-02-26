import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [0 for _ in range(m)]
visited = [False for _ in range(n + 1)]


def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        arr[cur] = i
        recur(cur + 1)
        arr[cur] = 0
        visited[i] = False


recur(0)
