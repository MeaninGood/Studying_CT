import sys
input = lambda : sys.stdin.readline().strip()

a, b, d = map(int, input().split(' '))

sieve = [True for _ in range(b + 1)]
sieve[0], sieve[1] = False, False 
for i in range(2, b + 1):
    if i * i > b + 1:
        break
    
    for j in range(i * i, b + 1, i):
        sieve[j] = False
        
cnt = 0
for i in range(a, b + 1):
    if str(d) in str(i) and sieve[i]:
        cnt += 1
        
print(cnt)