n, k = map(int, input())

arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)


cnt = 0

for i in range(n):
    if arr[i] > k:
        continue
        
    