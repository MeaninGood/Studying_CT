import sys
input = lambda : sys.stdin.readline().strip()

n, c, w = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = 0
cnt = arr[-1]

while cnt > 0:
    total = 0
    for tree in arr:
        tmp = (cnt * (tree // cnt) * w) - (c * ((tree // cnt) - ((tree % cnt) == 0)))
        if tmp < 0:
            continue
        total += tmp

    ans = max(total, ans)
    cnt -= 1
    
print(ans)