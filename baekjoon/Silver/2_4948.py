sieve = [True for _ in range(250000)]
sieve[0] = False
sieve[1] = False

for i in range(2, 250000):
    if not sieve[i]:
        continue
    
    for j in range(i * i, 250000, i):
        sieve[j] = False
        
  
while 1:
    a = int(input())
    
    if a == 0:
        break
    
    cnt = 0

    for j in range(a + 1, (2 * a) + 1):
        if sieve[j]:
            cnt += 1
            
    print(cnt)