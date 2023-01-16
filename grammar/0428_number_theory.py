# 0. 모듈러의 성질

# print(5 % 3)
#
# print((5 + 8) % 3)
# print((5 % 3 + 8 % 3) % 3)
#
# (a + b) % c == (a % c + b % c) % c
# (a * b) % c == (a % c * b % c) % c
# (a - b) % c == (a % c - b % c + 1000 * c) % c
# (a // b) % c == (a // c - b // c) % c  => 수학적으로는 되지만, 코딩할땐 안된다. 안된다고 생각하자. => 페르마 소정리 a^p % p == a
#
# int => 21억
# long, long long => 21억*21억*2
# 파이썬도 기본적으로 21억*21억*2(그 이상은 느려진다.)






# 1. 소수 판정 => 1 조심
# 자연수 하나를 입력 받아서 이 수가 소수면 YES, 소수가 아니면 NO를 출력한다.
# n제한이 일반적으로 10^12정도로 나온다.

# 12의 약수
# 1 2 3 4 6 12

# 1 12
# 2 6
# 3 4

# 왼쪽 <= 오른쪽     따라서 왼쪽 수는 모두 루트n 이하
# 1~루트n까지 약수가 정확히 하나인지 구한다.

# n = int(input())
#
# cnt = 0
# for i in range(2, n + 1):
#     if i * i > n:
#         break
#
#     if n % i == 0:
#         cnt += 1
#
# if n == 1:
#     print("NO")
# elif cnt == 0:
#     print("YES")
# else:
#     print("NO")





# 2. 약수 구하기 => 제곱수를 조심.
# 약수의 개수가 홀수 <=> 제곱수

# n = int(input())
# prime = []
#
# for i in range(1, n + 1):
#     if i * i > n:
#         break
#
#     if n % i == 0:
#         prime.append(i)
#         if i * i != n:
#             prime.append(n // i)
#
# print(*prime)





# 3. 소인수 분해 => 계산하는 변수랑 i * i보다 작은지 판단할 변수를 따로 둬야 한다.

# n => a, b, c, d, e, f, g, h, i
# a * b * c * d * e * f * g * h * i => n

# n = int(input())
#
# x = n
# for i in range(2, n + 1):
#     if i * i > n:
#         break
#
#     while x % i == 0:
#         print(i)
#         x //= i
#
# if x != 1:
#     print(x)




# 4. 유클리드 호제법 => GCD(최대공약수)를 구할 수 있는데, 응용을 조금 하면 LCM(최소공배수)도 구할 수 있다.
# 목표 : 두 자연수 a, b가 주어질 때 이 둘의 최대공약수를 구한다.(log n)

# a, b = map(int, input().split())
#
# A, B = a, b
# while a % b != 0:
#     a, b = b, a % b
#
# print(b)            #최대공약수
# print(A * B // b)   #최소공배수




# 5. 에라토스테네스의 체
# 목표 : 1~n까지의 자연수 중 소수를 모두 출력한다.

# n = int(input())
# isPrime = [True for i in range(n + 1)]
#
# isPrime[0] = False
# isPrime[1] = False
# for i in range(2, n + 1):
#     if not isPrime[i]:
#         continue
#
#     for j in range(i * i, n + 1, i):
#         isPrime[j] = False
#
# print(*[i for i in range(n + 1) if isPrime[i]])

# 응용 : 2~n까지의 자연수 각각의 가장 작은 소인수 출력

# n = int(input())
# prime = [-1 for i in range(n + 1)]
#
# for i in range(2, n + 1):
#     if prime[i] != -1:
#         continue
#
#     prime[i] = i
#     for j in range(i * i, n + 1, i):
#         if prime[j] == -1:
#             prime[j] = i
#
# print(*prime[2:])



# 6. 빠른 거듭제곱
# 목표 : (n ** m) % 1000000007 (n <= 100, m <= 1,000,000,000,000,000,000) 빠르게 구하기


# def pows(n, m):
#     if m == 0:
#         return 1
#
#     ret = pows(n, m // 2)
#     ret *= ret
#     ret %= 1000000007
#
#     if m % 2 == 0:
#         return ret
#     else:
#         return (ret * n) % 1000000007
#
