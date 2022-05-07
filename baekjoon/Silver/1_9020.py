sieve = [True for _ in range(10010)]
sieve[0] = False
sieve[1] = False

for i in range(2, 10010):
    if not sieve[i]:
        continue
    
    for j in range(i * i, 10010, i):
        sieve[j] = False

T = int(input())
for tc in range(T):
    n = int(input())
    
    a = 0
    b = 0
    for i in range(2, (n // 2) + 1):
        if sieve[i] and sieve[n - i]:
            a = i
            b = n - i
            
    print(a, b)