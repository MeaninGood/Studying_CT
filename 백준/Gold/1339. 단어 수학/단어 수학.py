import sys
input = lambda : sys.stdin.readline().strip()


n = int(input())
arr = [list(input()) for _ in range(n)]

d = {}
for i in range(n):
    idx = len(arr[i])
    for j in range(len(arr[i])):
        tmp = 10 ** (idx - 1)
        if d.get(arr[i][j]):
            d[arr[i][j]] += tmp
        
        else:
            d[arr[i][j]] = d.get(arr[i][j], tmp)
        
        idx -= 1
        
li = sorted(d.items(), key=lambda x : -x[1])

total = 0
idx = 9
for k, v in li:
    total += idx * v
    idx -= 1
    
print(total)