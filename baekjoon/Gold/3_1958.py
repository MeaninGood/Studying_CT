import sys
input = lambda : sys.stdin.readline().strip()
from pprint import pprint

arr1 = ['#'] + list(input())
arr2 = ['#'] + list(input())
arr3 = ['#'] + list(input())

n, m, z = len(arr1), len(arr2), len(arr3)

arr = [[[0 for i in range(z)] for j in range(m)] for k in range(n)]

answer = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(1, z):
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                arr[i][j][k] = arr[i - 1][j - 1][k - 1] + 1
                
            else:
                arr[i][j][k] = max(arr[i - 1][j][k], arr[i][j - 1][k], arr[i][j][k - 1])
            
            answer = max(answer, arr[i][j][k])

print(answer)

"""
dababcf
ababdef
df
"""