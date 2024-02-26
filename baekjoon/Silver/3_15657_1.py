import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

arr = [0 for _ in range(m)]


def recur(cur):
    if cur == m:
        print(*arr)
        return

    for i in range(n):
        if arr[cur - 1] > nums[i]:
            continue

        arr[cur] = nums[i]
        recur(cur + 1)
        arr[cur] = 0


recur(0)
