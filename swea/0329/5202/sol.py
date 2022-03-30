T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [-1 for _ in range(25)]
    
    def recur(cur):
        if dp[cur] != -1:
            return dp[cur]
        
        ret = 0
        
        for i in range(n):
            if cur <= arr[i][0]:
                ret = max(ret, recur(arr[i][1]) + 1)
                
        dp[cur] = ret
        return ret

    print(f'#{tc} {recur(0)}')




# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dp = [-1 for _ in range(25)]

# def recur(cur):
#     if dp[cur] != -1:
#         return dp[cur]
    
#     ret = 0
    
#     for i in range(n):
#         if cur <= arr[i][0]:
#             ret = max(ret, recur(arr[i][1]) + 1)
#             dp[cur] = ret
#             print(dp)
            
#     return ret

# print(f'#{recur(0)}')