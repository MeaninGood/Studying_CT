import sys
input = sys.stdin.readline

n = int(input())
arr = input().strip()

s = 0
e = 0
d = {arr[0]: 1}
cnt = 0
mx = 0

while s <= e and e < len(arr) - 1:
    
    if len(d) > n:
        d[arr[s]] -= 1
        
        if d[arr[s]] == 0:
            del d[arr[s]]
        
        s += 1

    else:
        e += 1
        d[arr[e]] = d.get(arr[e], 0) + 1
        
                    
        if len(d) <= n:
            mx = max(mx, sum(d.values()))
        
print(mx)