import sys

arr = [i for i in range(1, 13)]
ans = 1 << 12
def cur(n, k):
    for i in range(ans):
        cnt = 0
        res = 0
        for j in range(12):
            if i & (1<<j):
                cnt += 1
                res += j+1
        if cnt == n and res == k:
            res += 1

        return res




sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]

    print(cur(n, k))
