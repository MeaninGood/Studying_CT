'''
7
ABCD
Z
145C
CB
A
A910
Z321

'''
n = int(input())
arr = [input() for _ in range(n)]
arr.sort(key = lambda x: len(x))
print(arr)

v = []
mlen = len(arr[0])

for i in range(1, n):
    if len(arr[i]) > len(arr[i - 1]):
        continue
    
    if len(arr[i]) == len(arr[i - 1]):
        
         
    
