'''

'''

n = int(input())
arr = list(map(int, input().split()))

b = []
c = sorted(arr)

for idx, num in enumerate(c):
    b.append([idx, num])

b.sort(key = lambda x: x[1])

visited = [False for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[j]:
            continue
        
        if arr[i] == b[j][1]:
            visited[j] = True
            print(b[j][0], end = ' ')
            break
        