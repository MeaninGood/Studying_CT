import sys
input = lambda : sys.stdin.readline().strip()

arr = []

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue
            
            arr.append(str(i) + str(j) + str(k))
            

n = int(input())
m = len(arr)

visited = [True for _ in range(m)]
for i in range(n):
    ans, strk, ball = map(int, input().split())
    
    a, b, c = str(ans)[0], str(ans)[1], str(ans)[2]
    
    for j in range(m):
        if not visited[j]:
            continue
        
        scnt, bcnt = 0, 0
        
        x, y, z = arr[j][0], arr[j][1], arr[j][2]
        
        # strk 체크
        scnt += (a == x) + (b == y) + (c == z)
        
        # ball 체크
        bcnt += (a == y) + (a == z) + (b == x) + (b == z) + (c == x) + (c == y)
            
        if scnt != strk or bcnt != ball:
            visited[j] = False
            
    
ans = 0        
for i in range(m):
    if visited[i]:
        ans += 1
        
print(ans)