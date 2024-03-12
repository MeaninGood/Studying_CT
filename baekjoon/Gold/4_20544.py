import sys

sys.setrecursionlimit(10000)

input = lambda: sys.stdin.readline().strip()

n = int(input())

dp = [[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(3)] for _ in range(n)]

# 현재, 몇 개 연속이냐, 2짜리가 몇 개 연속이냐, 높이2가 1개 있나
def recur(cur, cnt1, cnt2, two):
    if cnt1 > 2 or cnt2 >= 2:
        return 0

    if cur == n:
        return two
    
    if dp[cur][cnt1][cnt2][two] != -1:
        return dp[cur][cnt1][cnt2][two]
    
    dp[cur][cnt1][cnt2][two] = recur(cur + 1, 0, 0, two) + recur(cur + 1, cnt1 + 1, 0, two) + recur(cur + 1, cnt1 + 1, cnt2 + 1, 1)
    dp[cur][cnt1][cnt2][two] %= 1000000007
    
    return dp[cur][cnt1][cnt2][two] 

print(recur(1, 0, 0, 0))
