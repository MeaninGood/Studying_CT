import sys

input = lambda: sys.stdin.readline().strip()


def getSum(mid, x, y):
    return prefix[mid] * x + suffix[mid] * y


def getResult(x, y):
    s, e = 0, 1000010
    res = 1 << 62

    while e >= s:
        mid = (s + e) // 2

        res = min(res, getSum(mid, x, y))

        if getSum(mid, x, y) > getSum(mid + 1, x, y):
            s = mid + 1

        else:
            e = mid - 1

    return res


n = int(input())
arr = sorted(list(map(int, input().split(" "))))

prefix, suffix = [0 for _ in range(1000010)], [0 for _ in range(1000010)]

cnt = 0
for i in range(1000010):
    if i > 0:
        prefix[i] = prefix[i - 1] + cnt

    while cnt < n and arr[cnt] == i:
        cnt += 1

cnt = n - 1
for i in range(1000009)[::-1]:
    suffix[i] = suffix[i + 1] + n - 1 - cnt

    while cnt >= 0 and arr[cnt] == i:
        cnt -= 1

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())

    print(getResult(x, y))
