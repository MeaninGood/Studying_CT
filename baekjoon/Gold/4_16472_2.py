import sys

input = lambda : sys.stdin.readline().strip()

k = int(input())
arr = list(input())
n = len(arr)

arr += ['#']

s, e = 0, 0
op = {arr[s]: 1}
length = 1
ans = 0
while e < n:
    if len(op) <= k:
        ans = max(ans, sum(op.values()))
        
        e += 1
        op[arr[e]] = op.get(arr[e], 0) + 1
        
    else:
        op[arr[s]] -= 1
        
        if op[arr[s]] == 0:
            del op[arr[s]]
            
        s += 1
        
print(ans)