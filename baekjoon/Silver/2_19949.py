import sys

input = lambda: sys.stdin.readline().strip()

arr = list(map(int, input().split()))

res = 0


def recur(cur, prv1, prv2, total):
    global res

    if cur == 10:
        if total >= 5:
            res += 1
        return

    for i in range(1, 6):
        if prv1 == prv2 == i:
            continue

        if arr[cur] == i:
            recur(cur + 1, prv2, i, total + 1)

        else:
            recur(cur + 1, prv2, i, total)


recur(0, 0, 0, 0)
print(res)
