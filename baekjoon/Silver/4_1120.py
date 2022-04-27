a, b = map(str, input().split())
    
la = len(a)
lb = len(b)

ans = 1000000000
for i in range(lb - la + 1):
    tmp = 0
    for j in range(la):
        if a[j] != b[i + j]:
            tmp += 1
        
    ans = min(ans, tmp)
    
print(ans)