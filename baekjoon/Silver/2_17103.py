sieve = [True for _ in range(1000010)]

sieve[0] = False
sieve[1] = False
for i in range(2, 1000010):
    if not sieve[i]:
        continue
    
    for j in range(i * i, 1000010, i):
        sieve[j] = False
        
T = int(input())
for tc in range(T):
    n = int(input())
    
    cnt = 0
    for i in range(1, n // 2 + 1):          
        if sieve[i] and sieve[n - i]:
            cnt += 1
            
    print(cnt)
