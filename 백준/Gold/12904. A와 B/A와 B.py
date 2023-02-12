import sys
input = lambda : sys.stdin.readline().strip()

arr1 = list(input())
arr2 = list(input())

n, m = len(arr1), len(arr2)
for i in range(m):
    if arr1 == arr2:
        print(1)
        break
    
    if len(arr1) >= len(arr2):
        print(0)
        break
    
    if arr2[-1] == 'A':
        arr2 = arr2[:-1]
        
    elif arr2[-1] == 'B':
        arr2 = arr2[:-1]
        arr2 = arr2[::-1]