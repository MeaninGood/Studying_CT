import sys

input = lambda: sys.stdin.readline().strip()

tc = int(input())


for _ in range(tc):
    k, n = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = [arr[0] for _ in range(n)]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    d = {}
    ans = 0
    for i in range(n):
        if prefix[i] % k == 0:
            ans += 1
        target = prefix[i] % k
        ans += d.get(target, 0)
        d[target] = d.get(target, 0) + 1
            
    print(ans)