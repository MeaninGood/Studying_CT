n = int(input())

cnt = 0
for a in range(1, n):
    if a % 2:
        continue
    
    for b in range(1, n):
        c = n - (a + b)
        
        if c < (b + 2):
            continue
        
        cnt += 1
        
print(cnt)