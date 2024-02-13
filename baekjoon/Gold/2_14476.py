import sys

input = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a % b != 0:
        a, b = b, a % b
        
    return b

n = int(input())
arr = sorted(list(map(int, input().split())))

prefix = [0 for _ in range(n)]
suffix = [0 for _ in range(n)]
prefix[0] = arr[0]
suffix[-1] = arr[-1]

for i in range(1, n):
    prefix[i] = gcd(prefix[i - 1], arr[i])
    
for i in range(n - 1)[::-1]:
    suffix[i] = gcd(suffix[i + 1], arr[i])
    
res, num = suffix[1], arr[i]

for i in range(1, n):
    if i == n - 1:
        if res < prefix[n - 2]:
            res = prefix[n - 2]
            num = arr[i]
            
    else:
        tmp = gcd(prefix[i - 1], suffix[i + 1])
        if res < tmp:
            res = tmp
            num = arr[i]
    
if num % res == 0:
    print(-1)

else:
    print(res, num)