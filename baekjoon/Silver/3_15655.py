import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [0 for _ in range(m)]


def recur(cur, s):
    if cur == m:
        print(*arr)
        return

    for i in range(s, n):
        arr[cur] = nums[i]
        recur(cur + 1, i + 1)


recur(0, 0)
