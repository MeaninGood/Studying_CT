n = int(input())
papers = [list(map(int, input().split(' '))) for _ in range(n)]

arr = [[False for _ in range(110)] for _ in range(110)]
for x, y in papers:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = True

cnt = 0     
for i in range(110):
    for j in range(110):
        if arr[i][j]:
            cnt += 1
            
print(cnt)