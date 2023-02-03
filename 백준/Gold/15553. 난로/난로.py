import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]


idx = [0 for _ in range(n - 1)]
for i in range(n - 1):
    idx[i] = arr[i + 1] - arr[i]
    
idx.sort()

answer = 0
for i in range(n - m):
    answer += idx[i]
    
print(answer + m)