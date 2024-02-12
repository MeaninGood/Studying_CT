import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 100000000
for i in range(n):
    mn1 = 1 << 30
    mn2 = 1 << 31
    
    for j in range(n):
        if i == j:
            continue
        
        tmp = abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) + abs(arr[i][2] - arr[j][2])

        if mn1 >= tmp:
            mn2 = mn1
            mn1 = tmp   

        elif mn2 >= tmp:
            mn2 = tmp
            
    ans = min(ans, mn1 + mn2)
    
print(ans)