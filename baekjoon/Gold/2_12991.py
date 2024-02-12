import sys

input = lambda: sys.stdin.readline().strip()

def bin_search(target):
    cnt = 0

    for i in range(n):
        s, e = 0, n - 1

        while s <= e:
            mid = (s + e) // 2

            if a[i] * b[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        cnt += s

    return cnt

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

s, e = a[0] * b[0], a[n - 1] * b[n - 1]

while s <= e:
    mid = (s + e) // 2

    target = bin_search(mid)

    if target < k:
        s = mid + 1
    else:
        e = mid - 1

print(s)