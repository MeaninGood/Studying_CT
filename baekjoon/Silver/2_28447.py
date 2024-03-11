import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
visited = [False for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def recur(cur, cnt):

    if cur > n or cnt > k:
        return -10000000000

    if cur == n:
        total = 0
        if cnt == k:
            # 고른 애들만 보기
            for i in range(n - 1):
                if not visited[i]:
                    continue

                for j in range(i + 1, n):
                    if not visited[j]:
                        continue

                    total += arr[i][j]

        return total

    if dp[cur][cnt] != -1:
        return dp[cur][cnt]

    visited[cur] = True
    ntotal1 = recur(cur + 1, cnt + 1)
    visited[cur] = False
    ntotal2 = recur(cur + 1, cnt)

    dp[cur][cnt] = max(ntotal1, ntotal2)

    return dp[cur][cnt]


print(recur(0, 0))
