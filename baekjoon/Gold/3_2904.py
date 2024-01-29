import sys
input = lambda: sys.stdin.readline().strip()

# t = 1000010
# sieve = [True for _ in range(t)]
# sieve[0], sieve[1] = False, False

# for i in range(2, t):
#     if i * i > t:
#         break
    
#     for j in range(i * 2, t, i):
#         sieve[j] = False
        
        
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    
    while a % b != 0:
        a, b = b, a % b
        
    return b


n = int(input())
arr = list(map(int, input().split()))

arr.sort()
score = gcd(arr[0], arr[1])
for i in range(2, n):
    score = min(score, gcd(score, arr[i]))
    
print(score)
