# 시간복잡도 줄이기랑, 메모리 줄이기 + 다른 알고리즘을 설명할 때 base가 됨

# 0. 모듈러의 성질
# print(5 % 3)
# print((5 + 8) % 3)
# print((5 % 3 + 8 % 3) % 3)
"""
n = a c + d
a : // /
d 찾기 : %

n // c = a
n % c = d

a = xc + y
b = wc + z
a + b = (x + w)c + y + z

(a + b) % c = (a % c + b % c) % c
(a - b) % c = (a % c - b % c + 1000 * c) % c

(6 - 3) % 5 == 3
(6 % 5 - 3 % 5) % 5 // 5 % 5 = 0과 같은 것. 25 % 5 = 0과 같은 개념
(1 - 3 + 5) % 5
(-2) % 5 => 음수
(3) % 5 = > 3

(a * b) % c = (a % c * b % c) % c

(a // b) % c == 수학적으로는 돼. 근데 코딩에서는 안 돼 => 안됨
역원을 구하는 개념 페르마 소정리 a^p % p == a 코딩 대회에서나 나오고 몰라도 돼

더하기, 빼기(주의), 곱하기는 되지만 나누는 건 안 된다
"""

# 파이썬을 제외하면 모두 int 자료형을 지정
# int => 21억 정도
# long, BigInteger => 21억 * 21억 * 2
# 파이썬에서도 21억 * 21억 * 2
# 숫자가 커지면 연산이 느려짐 !!
# 정말 큰 숫자 연산해야 되는 경우, % 10000000007 ==> 답으로 인정하겠다

# 1부터 100000000000 합의 % 10000000007을 출력해라
# total = 0
# for i in range(1, 100000000001):
#     total += i
#     total %= 10000000007

# print(total % 10000000007)


# 1. 소수판정 => 1을 처리하는 것
# 자연수 하나를 입력 받아서 이 수가 소수면 YES, 아니면 NO
# n제한 10^12 정도로 온다

"""
12의 약수
1 2 3 4 6 12

1 12
2 6
3 4
왼쪽 < 오른쪽 "왼쪽 수는 모두 루트n 이하"
# 왼쪽 x 오른쪽 = n이 된다
1~루트n까지 약수가 정확하게 하나인지 아닌지만 보면 된다.
"""

# n = int(input())
# cnt = 0
# 1은 소수가 아님

# for i in range(1, n + 1):
#     if i * i > n:
#         break
    
#     if n % i == 0:
#         cnt += 1
        
# if n == 1:
#     print('NO')  
# elif cnt == 1:
#     print('YES')
# else:
#     print('NO')


# 2. 약수 구하기 => 제곱수를 주의
# 약수의 개수가 홀수다 == 제곱수다
# n = int(input())
# prime = []

# for i in range(1, n + 1):
#     if i * i > n:
#         break
    
#     if n % i == 0:
#         prime.append(i)
        
#         if i * i != n:
#             prime.append(n // i)
        
# print(prime)
"""
1 5 25 => 홀수개

"""
# 3. 소인수분해 => 계산하는 변수랑 i * i보다 작은지 판단할 변수를 따로 둬야 함
# 소인수 모두 다 출력하기
# n => a * b * c * d * e * f * g * h * i = n
# 12 => 2 * 2 * 3
# 1 2 3 4 6 12
# 57 = 3 * 19 => 19
# i = 8 
# n = int(input())

# x = n
# # 1은 소수가 아니기 때문에
# for i in range(2, n + 1):
#     if i * i > n:
#         break
    
#     while x % i == 0:
#         print(i)
#         x //= i
        
# if x != 1:
#     print(x)


# 4. 유클리드 호제법 (logn의 시간복잡도) => gcd(최대공약수)를 구할 수 있는데, 응용해서 lcm(최소공배수)도 구할 수 있다!
# 두 자연수 a, b가 주어질 때 이 둘의 최대공약수 구하기
"""
a, b = b, a - b
44 8
    8 36
    8 28
    8 20
    8 12
8 4

a, b = b, a % b

"""
a, b = map(int, input().split())

A, B = a, b
while a % b != 0:
    a, b = b, a % b
    print(a, b)
    
print(b) # 최대공약수
print(A * B // b) # 최소공배수
"""
최소공배수 구하기

2^3 3^2 5^2
2^2 3^6      7^3
최대공약수 : 2^2 3^2 작은 것만 고른 것
최소공배수 : 2^3 3^6 5^2 7^3 큰 것만 고른 것
2^5 3^8 5^2 7^3 // 2^2 3^2
2^3 3^6 5^2 7^3
"""

# 5. 에라토스테네스의 체
# 목표 : 1~n까지의 자연수 중 소수를 모두 출력한다.
# 10 => 1(x) 2, 3, 5, 7
# n = int(input())
# sieve = [True for i in range(n + 1)]

# sieve[0] = False
# sieve[1] = False

# for i in range(2, n + 1):
#     if not sieve[i]:
#         continue
    
#     # i부터 n + 1까지 i간격으로 돈다
#     # 2 4 6 8 10 12 14 ...
#     for j in range(i * i, n + 1, i):
#         sieve[j] = False
"""
1   2   3   4   5   6   7   8   9   10 
o   o   o   x   o   x   o   x   x   x
11  12  13  14  15  16  17  18  19  20
o   x   o   x   x   x   o   x   o   x
21  22  23  24  25  26  27  28  29  30
x   x   o   x   x   x   x   x   o   x
"""

# 응용 : 2~n까지의 자연수 각각의 가장 작은 소인수 출력
n = int(input())
prime = [-1 for _ in range(n + 1)]
for i in range(2, n + 1):
    if prime[i] != -1:
        continue
    
    prime[i] = i
    for j in range(i * i, n + 1, i):
        if prime[j] == -1:
            prime[j] = i
            
print(*prime[2:])
"""
1   2   3   4   5   6   7   8   9   10 
-1  2   3  2  -1  2  -1  2  3  2
11  12  13  14  15  16  17  18  19  20
-1  2  -1  -2  3  -1  -1  2  -1  -1

"""

# 6. 빠른 거듭제곱
# 목표 : n ** m % 1000000007 (n <= 100, m <= 1,000,000,000,000,000,000,000)
n, m = map(int, input().split())
print(pow(n, m, 1000000007))

def pows(n, m):
    if m == 0:
        return 1
    
    ret = pows(n, m // 2)
    ret *= ret
    ret %= 1000000007
    
    if m % 2 == 0:
        return ret
    
    else:
        return (ret * n) % 1000000007
