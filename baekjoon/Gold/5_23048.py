import sys
input = sys.stdin.readline

n = int(input())

sieve = [True for i in range(n + 1)]

sieve[0] = False
sieve[1] = False

idx = 1
v = [1 for i in range(n + 1)]
for i in range(2, n + 1):
    if not sieve[i]:
        continue
    
    idx += 1
    v[i] = idx
    for j in range(i * i, n + 1, i):
        sieve[j] = False
        v[j] = idx
    
    
v.pop(0)
print(idx)
print(*v)
    
