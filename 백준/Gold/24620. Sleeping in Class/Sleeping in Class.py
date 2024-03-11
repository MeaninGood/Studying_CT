import sys

input = lambda: sys.stdin.readline().strip()

def get_cnt(arr, target):
    total, cnt = 0, 0
    for a in arr:
        if total > target:
            return 0

        total += a
        if total == target:
            total = 0
            continue

        cnt += 1

    return cnt


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    s, e = max(arr), sum(arr)

    if e == 0:
        print(0)
        continue

    ans = 0
    for i in range(s, e + 1):
        if e % i != 0:
            continue

        cnt = get_cnt(arr, i)
        if cnt:
            ans = cnt
            break

    print(ans)