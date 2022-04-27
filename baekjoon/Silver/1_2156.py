import sys
sys.setrecursionlimit(100010)


n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [[-1, -1, -1] for _ in range(100010)]

def recur(cur, cnt):
    ret = 0
    
    if cnt > 2:
        return -10000000
    
    if dp[cur][cnt] != -1:
        return dp[cur][cnt]
    
    if cur >= n:
        return 0
    
    ret = max(recur(cur + 1, cnt + 1) + arr[cur], recur(cur + 1, 0))
    dp[cur][cnt] = ret
    return dp[cur][cnt]
              
print(recur(0, 0))
