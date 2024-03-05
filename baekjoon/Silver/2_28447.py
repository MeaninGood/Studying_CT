import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
visited = [False for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def recur(cur, cnt):
    ret = 0

    if cur > n:
        return -10000000000

    if cur == n:
        if cnt == k:
            # 고른 애들만 보기
            for i in range(n - 1):
                if not visited[i]:
                    continue

                for j in range(i + 1, n):
                    if not visited[j]:
                        continue

                    ret += arr[i][j]

            print(ret)

        return ret

    if dp[cur][cnt] != -1:
        return dp[cur][cnt]

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        dp[cur][cnt] = max(recur(cur + 1, cnt + 1), dp[cur][cnt])
        visited[i] = False

    return dp[cur][cnt]


print(recur(0, 0))
