def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    ans = gcd(a, b)
    print(a * b // ans)