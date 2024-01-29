import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())

sieve = [True for _ in range(n + 1)]
sieve[0], sieve[1] = False, False

for i in range(2, n + 1):
    if i * i > n:
        break
    
    for j in range(i + i, n + 1, i):
        sieve[j] = False
        
arr = []
for i in range(n + 1):
    if sieve[i]:
        arr.append(i)

length = len(arr)
arr += [0]

s, e = 0, 0
ans = 0
total = arr[s]
while e < length:
    if total == n:
        ans += 1
        total -= arr[s]
        s += 1
        e += 1
        total += arr[e]
        
    elif total > n:
        total -= arr[s]
        s += 1
        
    else:
        e += 1
        total += arr[e]
        
print(ans)