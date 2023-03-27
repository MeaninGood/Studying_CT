def check(arr):
    d = {}
    for i in range(0, len(arr) - 1):
        d[arr[i]] = d.get(arr[i], 0) + 1
        
        if arr[i + 1] != arr[i] and arr[i + 1] in d:
            return 0
        
    return 1

n = int(input())
ans = 0
for i in range(n):
    arr = list(input())
    
    ans += check(arr)
    
print(ans)