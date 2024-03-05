import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
disc = {}
for i in range(n):
    cnt = int(input())
    tmp = []
    for j in range(cnt):
        info = list(map(int, input().split()))
        tmp.append(info)

    disc[i] = disc.get(i, tmp) + []

ans = 1 << 31

visited = [False for _ in range(n)]
dp = [[1 << 31 for _ in range(n + 1)] for _ in range(n + 1)]


def recur(cur, total, tmp_arr, cnt):
    if cur > n or cnt > n:
        return 1 << 31

    if cur == n:
        if cnt == n:
            return total

        return 1 << 31

    if dp[cur][cnt] != 1 << 31:
        return dp[cur][cnt]

    for i in range(n):
        if visited[i]:
            continue

        # 고른다 - 금액 빼주기
        new_arr = tmp_arr[:]
        for target, dis in disc[i]:
            new_arr[target - 1] = max(tmp_arr[target - 1] - dis, 1)
        visited[i] = True
        ntotal1 = recur(cur + 1, total + tmp_arr[i], new_arr, cnt + 1)
        visited[i] = False
        # 안 고른다
        ntotal2 = recur(cur + 1, total, tmp_arr, cnt)

        dp[cur][cnt] = min(ntotal1, ntotal2)

    return dp[cur][cnt]


print(recur(0, 0, arr, 0))
