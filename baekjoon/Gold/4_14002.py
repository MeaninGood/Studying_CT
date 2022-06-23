import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]
prv = [-1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prv[i] = j
            
mx = -1
idx = -1
for i in range(n):
    if mx < dp[i]:
        mx = dp[i]
        idx = i

print(max(dp))        
ans = []
while idx != -1:
    ans.append(idx)
    idx = prv[idx]

for i in ans[::-1]:
    print(arr[i], end = ' ')