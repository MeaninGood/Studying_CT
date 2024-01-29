import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [0] + list(map(int, input().split()))

visited = [True for _ in range(n + 1)]
for i in range(1, n + 1):
    if arr[i] < arr[i - 1]:
        visited[i] = False
    
ans = 0
for i in range(1, n + 1):
    if not visited[i]:
        ans += 1
        continue
    
    if visited[i - 1] and visited[i + 1] and arr[i - 1] <= arr[i + 1]:
        pass
print(visited)