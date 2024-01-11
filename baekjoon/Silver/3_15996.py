import sys
input = lambda : sys.stdin.readline().strip()

n, a = map(int, input().split(' '))

ans = 0
while n // a != 0:
    n //= a
    ans += n
    
print(ans)