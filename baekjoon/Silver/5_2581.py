sieve = [True for i in range(10010)]
sieve[0] = False
sieve[1] = False

for i in range(2, 10010):
    if not sieve[i]:
        continue
    
    for j in range(i * i, 10010, i):
        sieve[j] = False
        
        
n = int(input())
m = int(input())
cnt = 0
total = 0
mn = 100000000
for i in range(n, m + 1):
    if sieve[i]:
        cnt += 1
        total += i
        mn = min(i, mn)

if cnt == 0:
    print(-1)
else:
    print(total)
    print(mn)