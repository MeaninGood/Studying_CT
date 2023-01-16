import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())

arr = [list(input()) for _ in range(n)]

idx1 = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
idx2 = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

cnti = n - 8 + 1
cntj = m - 8 + 1
x, y = 0, 0

ans = 100000000
while x < cnti:
    while y < cntj:
        for k in range(2):
            cnt = 0
            if k == 0:
                for i in range(x, 8 + x):
                    for j in range(y, 8 + y):
                        if i % 2:
                            if arr[i][j] != idx1[j - y]:
                                cnt += 1
                        else:
                            if arr[i][j] != idx2[j - y]:
                                cnt += 1
                ans = min(ans, cnt)
                
            else:
                for i in range(x, 8 + x):
                    for j in range(y, 8 + y):
                        if i % 2:
                            if arr[i][j] != idx2[j - y]:
                                cnt += 1
                        else:
                            if arr[i][j] != idx1[j - y]:
                                cnt += 1
                                
                ans = min(ans, cnt)
        y += 1
    x += 1
    y = 0
        
print(ans)