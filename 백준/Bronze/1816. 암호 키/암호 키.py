import sys
input = lambda : sys.stdin.readline().strip()

isPrime = [True for _ in range(1000001)]

for i in range(2, 1000001):
    if not isPrime[i]:
        continue
    
    for j in range(i * i, 1000001, i):
        isPrime[j] = False
        
        
n = int(input())
for _ in range(n):
    num = int(input())
    
    flag = True
    for i in range(2, 1000001):
        if not isPrime[i]:
            continue
        
        if num % i == 0:
            flag = False
            break
        
    print('YES' if flag else 'NO')