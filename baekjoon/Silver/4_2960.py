import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sieve = [True for i in range(n + 1)]
sieve[0] = False
sieve[1] = False

cnt = 0
for i in range(2, n + 1):
    if not sieve[i]:
        continue
    
    for j in range(i, n + 1, i):
        if not sieve[j]:
            continue
        
        sieve[j] = False
        cnt += 1

        if cnt == m:
            print(j)
            exit()
