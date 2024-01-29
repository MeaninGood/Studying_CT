import sys
input = lambda : sys.stdin.readline().strip()

a, b = map(int, input().split(' '))

def get_palindrome(x, v):
    ret = x

    if (v != -1):
        ret = ret * 10 + v
        
    while x > 0:
        ret = 10 * ret + x % 10
        x //= 10
        
    return ret

def isPrime(x):
    for i in range(2, x):
        if i * i > x:
            break
        
        if x % i == 0:
            return False
        
    return x >= 2

cnt = 0
arr = []
# 짝수자리 팰린드롬 만들기
for i in range(1, 10000):
    num = get_palindrome(i, -1)
    
    if (a <= num <= b and isPrime(num)):
        arr.append(num)
# # 홀수자리 팰린드롬 만들기
for i in range(1000):
    for j in range(10):
        num = get_palindrome(i, j)
        
        if (a <= num <= b and isPrime(num)):
          arr.append(num)

arr.sort()
for i in arr:
    print(i)
    
print(-1)