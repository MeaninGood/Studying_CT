import sys
input = lambda : sys.stdin.readline().strip()

arr1 = ['#'] + list(input())
arr2 = ['#'] + list(input())

n, m = len(arr1), len(arr2)
arr = [[0 for i in range(m)] for j in range(n)]

answer = 0
for i in range(1, n):
    for j in range(1, m):
        if arr1[i] == arr2[j]:
            arr[i][j] = arr[i - 1][j - 1] + 1
            
        answer = max(answer, arr[i][j])
        
print(answer)